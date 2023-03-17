import datetime

import pytest
from django.test.client import Client
from django.urls import reverse

from users.models import User


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
def test_lot_data():
    return {
        "name": "Test lot",
        "description": "Test description",
        "monobank_jar_link": "jar/test_qweqe",  # has to be 'jar/xxxxxxxxxx'
        "ending_date": datetime.datetime.now() + datetime.timedelta(days=5),
    }


@pytest.fixture
def admin_user_credentials(admin_user):
    return {"username": admin_user.username, "password": "password"}


@pytest.fixture
def test_user_instance(test_user_data):
    return User.objects.create(**test_user_data)


@pytest.fixture
def admin_client_with_jwt(admin_user_credentials):
    user = User.objects.filter(username=admin_user_credentials["username"]).first()
    user.api_token = "api_token_test"
    user.save()

    admin_client_with_jwt = Client()
    auth_data = admin_client_with_jwt.post(path=reverse("login"), data=admin_user_credentials).json()

    admin_client_with_jwt.defaults["HTTP_AUTHORIZATION"] = f'Bearer {auth_data["access"]}'

    return admin_client_with_jwt
