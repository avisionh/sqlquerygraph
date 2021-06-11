import logging
import os
import argparse

from py2neo import Graph


logging.basicConfig(
    level=logging.INFO,
    filename="log/loader.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

NEO4J_AUTH = (os.getenv(key="NEO4J_USERNAME"), os.getenv(key="NEO4J_PASSWORD"))

g = Graph(uri="bolt://neo4j:7687", auth=NEO4J_AUTH)


if __name__ == """__main__""":
    argp = argparse.ArgumentParser()
    argp.add_argument("-f", "--file", type=str, help="Path for where Cypher query is.")
    args = argp.parse_args()

    logging.info(f"Reading {args.file}\n")
    with open(file=args.file, mode="r") as f:
        queries = f.read()

    logging.info(f"Formatting {args.file} for importing into neo4j\n")
    queries = queries.split(sep=";")
    queries = [txt for txt in queries if txt != "\n"]

    logging.info(f"Executing {args.file} in neo4j\n")
    for query in queries:
        g.evaluate(cypher=query)
