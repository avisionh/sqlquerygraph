import pytest


pytest_plugins = [
    "tests.fixtures.fixture_extractor",
    "tests.fixtures.fixture_exporter",
]


@pytest.fixture()
def extracted_analytics():
    return {
        "analytics.repo": [
            "github_repos.commits",
            "github_repos.languages",
            "github_repos.licenses",
        ],
        "analytics.author": ["github_repos.commits"],
        "analytics.committer": ["github_repos.commits"],
        "analytics.commit": ["github_repos.commits"],
        "analytics.user": ["analytics.author", "analytics.committer"],
    }
