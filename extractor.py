from typing import Union

import os
import re
from tqdm import tqdm

from moz_sql_parser import parse
from pprint import pprint


class Extractor:
    """
    Extract table names from SQL queries.

    :param script_dir: String of the directory were we store our SQL queries.
    :param schema: String of the dataset/schema that the SQL queries creating the table belongs to.
    """

    def __init__(self, script_dir: str, schema: str):
        self.script_dir = script_dir
        self.schema = schema

    def read_query(self, file: str) -> str:
        """
        Reads a SQL file in.

        :param file: String of the file to read query from.
        :return: String of the SQL query from the file.
        """
        _, file_extension = os.path.splitext(p=file)
        if file_extension == ".sql":
            with open(file=os.path.join(self.script_dir, file), mode="r") as f:
                query = f.read()
            return query
        else:
            raise Exception(
                f"Passed in a {file_extension} file. \n"
                f"Please pass in a .sql file instead."
            )

    @staticmethod
    def clean_query(query: str, str_to_remove: Union[str, list]) -> str:
        """
        Cleans a query so it can be parsed.

        :param query: String of the query to clean.
        :param str_to_remove: String or list of strings to remove from the query.
        :return: String of the cleaned query to parse.
        """
        # remove new lines and multiple spaces
        query = query.replace("\n", " ")
        query = re.sub(pattern=r"\s+", repl=" ", string=query)

        if str_to_remove is not None:
            for txt in str_to_remove:
                query = query.replace(txt, "")

        return query

    @staticmethod
    def parse_query(query: str, print_tree: bool = False) -> dict:
        """
        Parse a query into a JSON parse-tree.

        :param query: String of the SQL query to parse as a JSON parse-tree.
        :param print_tree: Boolean to print the JSON parse-tree.
        :return: Dictionary of the query as a JSON parse-tree.
        """
        query_json = parse(sql=query)
        if print_tree:
            pprint(object=query_json)
        return query_json

    @staticmethod
    def extract_from_json(obj: dict, key: str) -> list:
        """
        Recursively fetch values from a nested JSON.

        For our purposes, extract where key is 'from' allows extraction of *most* table names after a `FROM` clause.
            - It does not extract the table names when the name is nested in a subquery.
            - Nor does it extract table names in '<TYPE> JOIN` clauses.
        To achieve above two, need to extract where the key is 'value' and compare with actual table names.
        This is because the values returned when key is 'value' are table names, column names etc.
        Reference
            -  https://hackersandslackers.com/extract-data-from-complex-json-python/
        :param obj: Dictionary to extract values from.
        :param key: String of the value you want to extract.
        :return: List of values for the key.
        """
        arr = []

        def extract(obj: Union[dict, list], arr: list, key: str) -> list:
            """
            Recusively search for values of key in a JSON tree.

            :param obj: Dictionary to extract values from.
            :param arr: List to store extracted values to.
            :param key: String of the dictionary key to extract associated value from.
            :return: List of the extracted values.
            """
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(v, (dict, list)):
                        extract(obj=v, arr=arr, key=key)
                    elif k == key:
                        arr.append(v)
            elif isinstance(obj, list):
                for item in obj:
                    extract(obj=item, arr=arr, key=key)
            return arr

        values = extract(obj=obj, arr=arr, key=key)
        return values

    def extract_table_dependencies_from_queries(
        self,
        reference_datasets: list,
        str_to_remove: Union[str, list] = None,
        verbose: bool = False,
    ) -> dict:
        """
        Extracts the table names and their dependencies from a set of .sql files.

        :param reference_datasets: List of datasets/schema that the tables belong to.
        :param str_to_remove: String or list of strings to remove from the query.
        :param verbose: Boolean to output steps taken and query after cleaning. Useful for debugging.
        :return: Dictionary of tables as keys and their dependent tables as values.
        """
        queries, jsons, dicts = {}, {}, {}
        reference_datasets = tuple([f"{txt}." for txt in reference_datasets])
        for file_name in tqdm(os.listdir(path=self.script_dir)):

            if verbose:
                print(f"Reading query {file_name}...\n")
            query = self.read_query(file=file_name)
            queries[file_name] = query

            if str_to_remove is not None:
                if verbose:
                    print(
                        f"Cleaning query {file_name} by removing {str_to_remove}...\n"
                    )
                queries[file_name] = self.clean_query(
                    query=queries[file_name], str_to_remove=str_to_remove
                )

            if verbose:
                print(f"Cleaned query is {queries[file_name]}")
                print(f"Parsing query {file_name}...\n")
            jsons[file_name] = self.parse_query(
                query=queries[file_name], print_tree=verbose
            )

            if verbose:
                print(f"Extracting table names from {file_name}...\n")
            #   - from: tables after 'from' clause
            #       + though sometimes keys are not 'from' so need to
            #       + look at values associated to the 'value' key
            #   - value: tables after '... join' clauses
            #       + can also include tables after 'from' clause if they
            #       + are in a subquery
            table_from = self.extract_from_json(obj=jsons[file_name], key="from")

            # keep only table elements and not table aliases - as defined by period
            table_from = [txt for txt in table_from if "." in txt]
            table_value = self.extract_from_json(obj=jsons[file_name], key="value")
            # extract table values when it starts with `<schema>.`
            table_join = [
                txt for txt in table_value if str(txt).startswith(reference_datasets)
            ]
            tables = list(set(table_from + table_join))

            # store in dictionary
            dicts[f"{self.schema}.{file_name}"] = tables

        return dicts
