import pytest


@pytest.fixture
def admin_user_credentials(admin_user):
    return {"username": admin_user.username, "password": "password"}
