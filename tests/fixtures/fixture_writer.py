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
        " CREATE CONSTRAINT table_name_ConstraintAnalytics ON (a:Analytics)\n"
        "ASSERT a.table_name IS UNIQUE;\n"
        " CREATE CONSTRAINT table_name_ConstraintGithubRepos ON (g:GithubRepos)\n"
        "ASSERT g.table_name IS UNIQUE;\n"
    )


@pytest.fixture()
def query_node_import():
    return (
        'USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///reporting_tables.csv" AS csvLine\n'
        "CREATE (:Reporting {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset), import_datetime: datetime()});\n"
        ' USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///analytics_tables.csv" AS csvLine\n'
        "CREATE (:Analytics {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset), import_datetime: datetime()});\n"
        ' USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///githubrepos_tables.csv" AS csvLine\n'
        "CREATE (:GithubRepos {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset), import_datetime: datetime()});\n"
    )
