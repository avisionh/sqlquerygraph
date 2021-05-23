import pytest


@pytest.fixture()
def query_user_activity():
    with open(file="data/reporting/user_activity.sql", mode="r") as f:
        return f.read()


@pytest.fixture()
def cleaned_user_activity():
    return (
        " WITH cte_base AS ( "
        "SELECT b.name ,b.email ,'commit' AS activity_type ,COUNT(a.*) AS activity_count "
        "FROM analytics.commit AS a "
        "LEFT JOIN analytics.user AS b "
        "ON a.committer_name = b.name "
        "AND b.user_type = 'committer' "
        "GROUP BY b.name ,b.email ,a.repo_name "
        "UNION "
        "SELECT a.author_name AS name ,b.email ,'repo' AS activity_type ,COUNT(a.*) AS activity_count "
        "FROM analytics.repo AS a "
        "LEFT JOIN analytics.user AS b "
        "ON a.author_name = b.name "
        "GROUP BY a.author_name ,b.email ) "
        "SELECT name ,email ,activity_type ,activity_count "
        "FROM cte_base "
        "UNION "
        "SELECT name ,email ,activity_type ,activity_count "
        "FROM ( "
        "SELECT name ,email ,'total' AS activity_type ,SUM(activity_count) AS activity_count "
        "FROM cte_base "
        "GROUP BY name ,email ) ; "
    )


@pytest.fixture()
def extracted_reporting():
    return {
        "reporting.user_activity": [
            "analytics.commit",
            "analytics.repo",
            "analytics.user",
        ]
    }
