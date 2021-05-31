import pytest


@pytest.fixture()
def datasets():
    return ["Reporting", "Analytics", "GitHub_Repos"]


@pytest.fixture()
def dir_file():
    return "neo4j"


@pytest.fixture()
def query_constraint():
    return (
        "CREATE CONSTRAINT table_name_ConstraintReporting ON (r:Reporting)\n"
        "ASSERT r.table_name IS UNIQUE;\n"
        "CREATE CONSTRAINT table_name_ConstraintAnalytics ON (a:Analytics)\n"
        "ASSERT a.table_name IS UNIQUE;\n"
        "CREATE CONSTRAINT table_name_ConstraintGitHub_Repos ON (g:GitHub_Repos)\n"
        "ASSERT g.table_name IS UNIQUE;\n"
    )


@pytest.fixture()
def query_node_import():
    return (
        'USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///reporting_tables.csv" AS csvLine\n'
        "CREATE (:Reporting {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset), import_datetime: datetime()});\n"
        'USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///analytics_tables.csv" AS csvLine\n'
        "CREATE (:Analytics {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset), import_datetime: datetime()});\n"
        'USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///github_repos_tables.csv" AS csvLine\n'
        "CREATE (:GitHub_Repos {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset), import_datetime: datetime()});\n"
    )


@pytest.fixture()
def query_rel():
    return (
        'USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///reporting_analytics_dependency.csv" AS csvLine\n'
        "MERGE (a:Reporting {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset)})\n"
        "MERGE (b:Analytics {table_name: toString(csvLine.dependency_name), table_dataset: toString(csvLine.dependency_dataset)})\n"
        "CREATE (a)-[:HAS_TABLE_DEPENDENCY {import_datetime: datetime()}]->(b);\n"
        'USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///reporting_github_repos_dependency.csv" AS csvLine\n'
        "MERGE (a:Reporting {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset)})\n"
        "MERGE (b:GitHub_Repos {table_name: toString(csvLine.dependency_name), table_dataset: toString(csvLine.dependency_dataset)})\n"
        "CREATE (a)-[:HAS_TABLE_DEPENDENCY {import_datetime: datetime()}]->(b);\n"
        'USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///analytics_analytics_dependency.csv" AS csvLine\n'
        "MERGE (a:Analytics {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset)})\n"
        "MERGE (b:Analytics {table_name: toString(csvLine.dependency_name), table_dataset: toString(csvLine.dependency_dataset)})\n"
        "CREATE (a)-[:HAS_TABLE_DEPENDENCY {import_datetime: datetime()}]->(b);\n"
        'USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///analytics_github_repos_dependency.csv" AS csvLine\n'
        "MERGE (a:Analytics {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset)})\n"
        "MERGE (b:GitHub_Repos {table_name: toString(csvLine.dependency_name), table_dataset: toString(csvLine.dependency_dataset)})\n"
        "CREATE (a)-[:HAS_TABLE_DEPENDENCY {import_datetime: datetime()}]->(b);\n"
    )
