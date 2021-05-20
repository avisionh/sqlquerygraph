import pytest


@pytest.fixture()
def extracted_user_activity():
    return {
        "reporting.user_activity": [
            "analytics.commit",
            "analytics.repo",
            "analytics.user",
        ]
    }
