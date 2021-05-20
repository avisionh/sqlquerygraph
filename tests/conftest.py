import pytest


pytest_plugins = [
    "tests.fixtures.fixture_extractor",
]


@pytest.fixture()
def query_user_activity():
    with open(file="data/reporting/user_activity.sql", mode="r") as f:
        return f.read()
