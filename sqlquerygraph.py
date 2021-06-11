import logging
import os
import argparse

from extractor import Extractor
import exporter
import writer

import numpy as np
import pandas as pd


logging.basicConfig(
    level=logging.INFO,
    filename="log/sqlquerygraph.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

if __name__ == """__main__""":
    argp = argparse.ArgumentParser()
    argp.add_argument(
        "-sd",
        "--script_dir",
        type=str,
        help="Directory where we store subdirectories of our SQL queries",
    )
    argp.add_argument(
        "-d",
        "--sub_dir",
        default=None,
        type=str,
        help="Subdirectories within script_dir that you want to read SQL queries from. "
        "If no value is inputted, then use all subdirectories in script_dir.",
    )
    argp.add_argument(
        "-rd",
        "--reference_datasets",
        nargs="*",
        type=str,
        default=[],
        help="Datasets that contain tables in database to look-up against. "
        "If no values is inputted, then take datasets specified in constants.py.",
    )
    argp.add_argument("-ed", "--export_dir", type=str, help="Directory to store files.")
    argp.add_argument(
        "-v",
        "--verbose",
        default=False,
        type=bool,
        help="Boolean to output steps taken and query after cleaning. "
        "Useful if want to check where function is failing.",
    )
    args = argp.parse_args()

    # initialise empty array for storing dfs
    arr = np.empty(shape=(0, 2))

    if args.sub_dir is None:
        subdir = os.listdir(path=args.script_dir)
    else:
        subdir = args.sub_dir
    print(subdir)

    for i, dataset in enumerate(subdir):

        logging.info(
            f"Extracting {dataset} tables and their dependencies from scripts\n"
        )
        # create text to remove
        dir_report = f"{args.script_dir}/{dataset}"
        remove_txt = []
        for table in os.listdir(dir_report):
            table_name, _ = os.path.splitext(p=table)
            remove_txt.append(f"MERGE {dataset}.{table_name} USING (")
        remove_txt.append(
            ") ON FALSE WHEN NOT MATCHED THEN "
            "INSERT ROW WHEN NOT MATCHED BY SOURCE THEN "
            "DELETE"
        )
        extractor = Extractor(script_dir=f"{args.script_dir}/{dataset}", schema=dataset)
        table_dependencies = extractor.extract_table_dependencies_from_queries(
            reference_datasets=args.reference_datasets,
            str_to_remove=remove_txt,
            verbose=args.verbose,
        )

        logging.info(f"Converting {dataset} dictionaries to dataframes\n")
        df_tables = exporter.convert_dict_to_df(data=table_dependencies)
        df_tables = df_tables.to_numpy()
        arr = np.concatenate((arr, df_tables), axis=0)

    logging.info("Splitting tables from their dependencies\n")
    df = pd.DataFrame(data=arr, columns=["table", "dependency"])
    df = exporter.separate_dataset_table(data=df)

    logging.info("Exporting unique table names for nodes\n")
    exporter.export_unique_names(data=df, path_or_buf=args.export_dir)

    logging.info("Exporting table dependencies for relationships\n")
    exporter.export_table_dependency(data=df, path_or_buf=args.export_dir)

    logging.info("Creating Cypher queries for neo4j database\n")
    datasets = [txt.title() for txt in args.reference_datasets]
    writer.create_query_constraint(datasets=datasets, dir_file=args.export_dir)
    writer.create_query_node_import(datasets=datasets, dir_file=args.export_dir)
    writer.create_query_relationship(datasets=datasets, dir_file=args.export_dir)
