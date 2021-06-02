import os
import argparse

from py2neo import Graph

NEO4J_AUTH = (os.getenv(key="NEO4J_USERNAME"), os.getenv(key="NEO4J_PASSWORD"))

g = Graph(auth=NEO4J_AUTH, host="localhost", port=7687, scheme="bolt")


if __name__ == """__main__""":
    argp = argparse.ArgumentParser()
    argp.add_argument("-f", "--file", type=str, help="Path for where Cypher query is.")
    args = argp.parse_args()

    print(f"Reading {args.file}\n")
    print("*******************************************\n")
    with open(file=args.file, mode="r") as f:
        queries = f.read()

    print(f"Formatting {args.file} for importing into neo4j\n")
    print("*******************************************\n")
    queries = queries.split(sep=";")
    queries = [txt for txt in queries if txt != "\n"]

    print(f"Executing {args.file} in neo4j\n")
    print("*******************************************\n")
    for query in queries:
        g.evaluate(cypher=query)
