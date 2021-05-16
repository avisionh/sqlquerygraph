from typing import Union

import os
import re

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
