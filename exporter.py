from typing import Union
import pandas as pd


def convert_dict_to_df(data: dict) -> pd.DataFrame:
    """
    Converts a dictionary into a dataframe, with keys and values being a column each.
    :param data: Dictionary to convert to a dataframe.
    :return: Dataframe where dictionary keys and values are a column.
    """
    data = pd.DataFrame.from_dict(data=data, orient="index").reset_index()
    data = data.rename(columns={"index": "table"})
    data = pd.melt(
        frame=data,
        id_vars="table",
        var_name="original_column_name",
        value_name="dependency",
    )
    # remove nans
    data = data[data["dependency"].notnull()]
    # sort values
    data = data.sort_values(by="table")

    return data[["table", "dependency"]]


def separate_dataset_table(data: Union[pd.Series, pd.DataFrame]) -> pd.DataFrame:
    """
    Separates string of <dataset>.<table_name> into dataset and table name.
    :param data: Dataframe with columns to separate string entries into dataset and table name.
    :return: Dataframe with columns for dataset and table name.
    """
    if isinstance(data, pd.Series):
        cols = "table"
    else:
        cols = data.columns

    for col in cols:
        col_names = [f"{col}_dataset", f"{col}_name"]
        # remove backslashes and split on period
        data[col] = data[col].str.replace(pat="\\", repl="", regex=True)
        data[col_names] = data[col].str.split(pat=".", n=1, expand=True)
        # remove full column
        data = data.drop(columns=col)

    return data


def export_unique_names(data: pd.DataFrame, path_or_buf: str):
    """
    Concatenates and unions a dataframe so we we get unique table names. This is so we create nodes in neo4j.
    :param data: Dataframe to get the names from.
    :param path_or_buf: String of the directory to store files.
    :return:
    """
    data_table = data[["table_dataset", "table_name"]]
    data_dependency = data[["dependency_dataset", "dependency_name"]]
    # rename so can union
    data_dependency = data_dependency.rename(
        columns={"dependency_dataset": "table_dataset", "dependency_name": "table_name"}
    )
    frames = [data_table, data_dependency]
    data_frames = pd.concat(objs=frames, axis="index")

    for ds in data_frames["table_dataset"].unique():
        df = data_frames[data_frames["table_layer"] == ds]
        df = df.drop_duplicates(subset="table_name")
        df.to_csv(path_or_buf=f"{path_or_buf}/{ds}_tables.csv", index=False)


def export_table_dependency(data: pd.DataFrame, path_or_buf: str):
    """
    Filters a dataframe by its table and dependency levels so it can be exported into neo4j.
    :param data: Dataframe to filter by table and dependency.
                Requires column to be called 'table_dataset' and 'dependency_dataset'.
    :param path_or_buf: String of the directory to store files.
    :return:
    """
    for t_ds in data["table_dataset"].unique():
        mask_t_ds = data["table_dataset"] == t_ds
        for d_ds in data["dependency_dataset"].unique():
            mask_d_ds = data["dependency_dataset"] == d_ds
            df_out = data.loc[
                (mask_t_ds & mask_d_ds),
            ]
            df_out = df_out.drop(columns=["table", "dependency"])
            df_out.to_csv(
                path_or_buf=f"{path_or_buf}/{t_ds}_{d_ds}_dependency.csv", index=False
            )
