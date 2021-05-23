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
