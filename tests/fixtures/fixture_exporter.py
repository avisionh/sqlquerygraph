import pytest
import pandas as pd


@pytest.fixture()
def dict_as_df():
    return pd.DataFrame(
        data={
            "table": [
                "analytics.author",
                "analytics.commit",
                "analytics.committer",
                "analytics.repo",
                "analytics.repo",
                "analytics.repo",
                "analytics.user",
                "analytics.user",
            ],
            "dependency": [
                "github_repos.commits",
                "github_repos.commits",
                "github_repos.commits",
                "github_repos.commits",
                "github_repos.languages",
                "github_repos.licenses",
                "analytics.author",
                "analytics.committer",
            ],
        }
    )


@pytest.fixture()
def df_separate_dataset_table():
    return pd.DataFrame(
        data={
            "table_dataset": [
                "analytics",
                "analytics",
                "analytics",
                "analytics",
                "analytics",
                "analytics",
                "analytics",
                "analytics",
            ],
            "table_name": [
                "author",
                "commit",
                "committer",
                "repo",
                "repo",
                "repo",
                "user",
                "user",
            ],
            "dependency_dataset": [
                "github_repos",
                "github_repos",
                "github_repos",
                "github_repos",
                "github_repos",
                "github_repos",
                "analytics",
                "analytics",
            ],
            "dependency_name": [
                "commits",
                "commits",
                "commits",
                "commits",
                "languages",
                "licenses",
                "author",
                "committer",
            ],
        }
    )
