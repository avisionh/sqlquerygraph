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
