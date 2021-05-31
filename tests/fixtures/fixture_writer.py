import pytest


@pytest.fixture()
def datasets():
    return ["Reporting", "Analytics", "GithubRepos"]


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
        "CREATE CONSTRAINT table_name_ConstraintGithubRepos ON (g:GithubRepos)\n"
        "ASSERT g.table_name IS UNIQUE;\n"
    )


@pytest.fixture()
def query_node_import():
    return (
        'USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///reporting_tables.csv" AS csvLine\n'
        "CREATE (:Reporting {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset), import_datetime: datetime()});\n"
        'USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///analytics_tables.csv" AS csvLine\n'
        "CREATE (:Analytics {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset), import_datetime: datetime()});\n"
        'USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///githubrepos_tables.csv" AS csvLine\n'
        "CREATE (:GithubRepos {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset), import_datetime: datetime()});\n"
    )


@pytest.fixture()
def query_rel():
    return (
        'USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///reporting_analytics_dependency.csv" AS csvLine\n'
        "MERGE (reporting:Reporting {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset)})\n"
        "MERGE (analytics:Analytics {table_name: toString(csvLine.dependency_name), table_dataset: toString(csvLine.dependency_dataset)})\n"
        "CREATE (reporting)-[:HAS_TABLE_DEPENDENCY {import_datetime: datetime()}]->(analytics);\n"
        'USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///reporting_githubrepos_dependency.csv" AS csvLine\n'
        "MERGE (reporting:Reporting {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset)})\n"
        "MERGE (githubrepos:GithubRepos {table_name: toString(csvLine.dependency_name), table_dataset: toString(csvLine.dependency_dataset)})\n"
        "CREATE (reporting)-[:HAS_TABLE_DEPENDENCY {import_datetime: datetime()}]->(githubrepos);\n"
        'USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///analytics_reporting_dependency.csv" AS csvLine\n'
        "MERGE (analytics:Analytics {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset)})\n"
        "MERGE (reporting:Reporting {table_name: toString(csvLine.dependency_name), table_dataset: toString(csvLine.dependency_dataset)})\n"
        "CREATE (analytics)-[:HAS_TABLE_DEPENDENCY {import_datetime: datetime()}]->(reporting);\n"
        'USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///analytics_githubrepos_dependency.csv" AS csvLine\n'
        "MERGE (analytics:Analytics {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset)})\n"
        "MERGE (githubrepos:GithubRepos {table_name: toString(csvLine.dependency_name), table_dataset: toString(csvLine.dependency_dataset)})\n"
        "CREATE (analytics)-[:HAS_TABLE_DEPENDENCY {import_datetime: datetime()}]->(githubrepos);\n"
        'USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///githubrepos_reporting_dependency.csv" AS csvLine\n'
        "MERGE (githubrepos:GithubRepos {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset)})\n"
        "MERGE (reporting:Reporting {table_name: toString(csvLine.dependency_name), table_dataset: toString(csvLine.dependency_dataset)})\n"
        "CREATE (githubrepos)-[:HAS_TABLE_DEPENDENCY {import_datetime: datetime()}]->(reporting);\n"
        'USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///githubrepos_analytics_dependency.csv" AS csvLine\n'
        "MERGE (githubrepos:GithubRepos {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset)})\n"
        "MERGE (analytics:Analytics {table_name: toString(csvLine.dependency_name), table_dataset: toString(csvLine.dependency_dataset)})\n"
        "CREATE (githubrepos)-[:HAS_TABLE_DEPENDENCY {import_datetime: datetime()}]->(analytics);\n"
    )
