import os


def create_query_constraint(datasets: list, dir_file: str) -> str:
    """
    Write query to create constraints in Cypher and export as .cypher file.

    :param datasets: List of datasets/schema to create constraints from.
    :param dir_file: String of the directory to store Cypher query in.
    :return: String of the queries in the script exported.
    """
    aliases = [txt[0].lower() for txt in datasets]
    cypher = []
    for name, alias in zip(datasets, aliases):
        query_constraint = (
            f"CREATE CONSTRAINT table_name_Constraint{name} ON ({alias}:{name})\n"
            f"ASSERT {alias}.table_name IS UNIQUE;\n"
        )
        cypher.append(query_constraint)

    cypher = "".join(cypher)
    with open(file=f"{dir_file}/query_constraints.cypher", mode="w") as f:
        f.write(cypher)

    return cypher


def create_query_node_import(datasets: list, dir_file: str) -> str:
    """
    Write query to create nodes in Cypher and export as .cypher file.

    :param datasets: List of datasets/schema to create nodes from.
    :param dir_file: String of the directory to store Cypher query in.
    :return: String of the queries in the script exported.
    """
    cypher = []
    for name in datasets:
        query_nodes = (
            f'USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///{name.lower()}_tables.csv" AS csvLine\n'
            f"CREATE (:{name} {{table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset), import_datetime: datetime()}});\n"  # noqa: E501
        )
        cypher.append(query_nodes)
    cypher = "".join(cypher)
    with open(file=f"{dir_file}/query_nodes.cypher", mode="w") as f:
        f.write(cypher)

    return cypher


def create_query_relationship(datasets: list, dir_file: str) -> str:
    """

    :param datasets:
    :param dir_file:
    :return:
    """
    aliases = [txt.lower() for txt in datasets]
    cypher = []
    for name, alias in zip(datasets, aliases):
        for sub_name, sub_alias in zip(datasets, aliases):
            file_name = f"{alias}_{sub_alias}_dependency.csv"
            if file_name not in os.listdir(path=dir_file):
                continue
            else:
                query_rel = (
                    f'USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///{file_name}" AS csvLine\n'  # noqa: E501
                    f"MERGE (a:{name} {{table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset)}})\n"  # noqa: E501
                    f"MERGE (b:{sub_name} {{table_name: toString(csvLine.dependency_name), table_dataset: toString(csvLine.dependency_dataset)}})\n"  # noqa: E501
                    f"CREATE (a)-[:HAS_TABLE_DEPENDENCY {{import_datetime: datetime()}}]->(b);\n"
                )
                cypher.append(query_rel)
    cypher = "".join(cypher)
    with open(file=f"{dir_file}/query_relationships.cypher", mode="w") as f:
        f.write(cypher)

    return cypher
