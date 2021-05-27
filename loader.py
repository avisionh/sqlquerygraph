def create_query_constraint(datasets: list, dir_file: str):
    """
    Write query to create constraints in Cypher and export as .cypher file.

    :param datasets: List of datasets/schema to create constraints from.
    :param dir_file: String of the directory to store Cypher query in.
    :return:
    """
    aliases = [txt[0].lower() for txt in datasets]
    cypher = []
    for name, alias in (datasets, aliases):
        query_constraint = (
            f"CREATE CONSTRAINT table_name_Constraint{name} ON ({alias}:{name}) "
            f"ASSERT {alias}.table_name IS UNIQUE;"
        )
        cypher.append(query_constraint)

    cypher = " ".join(cypher)
    with open(file=f"{dir_file}/query_constraints.cypher") as f:
        f.write(cypher)


def create_query_node_import(datasets: list, dir_file: str):
    """
    Write query to create nodes in Cypher and export as .cypher file.

    :param datasets: List of datasets/schema to create nodes from.
    :param dir_file: String of the directory to store Cypher query in.
    :return:
    """
    cypher = []
    for name in datasets:
        query_nodes = (
            f'USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///{name}_tables.csv" AS csvLine '
            f"CREATE (:Reporting {{table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset), import_datetime: datetime()}});"
        )  # noqa: E501
        cypher.append(query_nodes)
    cypher = " ".join(cypher)
    with open(file=f"{dir_file}/query_nodes.cypher") as f:
        f.write(cypher)
