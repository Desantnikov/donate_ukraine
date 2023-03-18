import pytest


@pytest.fixture
def expected_updated_test_user_data(test_user_data):
    updated_data = {key: f"updated_{value}" for key, value in test_user_data.items()}
    updated_data.pop("password")

    return updated_data
