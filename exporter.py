from typing import Union
import pandas as pd
import numpy as np


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
