import json

import pytest
from django.test.client import Client
from django.urls import reverse


@pytest.fixture
def test_user_data():
    return {
        "username": "test",
        "password": "pass",
        "email": "test@test.com",
        "phone_number": "1231231231",
        "api_token": "123testapitoken123",
    }


@pytest.fixture
def admin_user_credentials(admin_user):
    return {"username": admin_user.username, "password": "password"}


@pytest.fixture
def admin_client_with_jwt(admin_user_credentials):
    admin_client_with_jwt = Client()
    auth_data = admin_client_with_jwt.post(path=reverse("login"), data=admin_user_credentials).json()

    admin_client_with_jwt.defaults["HTTP_AUTHORIZATION"] = f'Bearer {auth_data["access"]}'

    return admin_client_with_jwt
