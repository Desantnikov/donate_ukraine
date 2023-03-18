import datetime

import pytest
from django.test.client import Client
from django.urls import reverse

from users.models import User
from users.serializers import UserSerializer


@pytest.fixture
def test_user_data():
    return {
        "username": "test",
        "password": "12345678",
        "email": "test@test.com",
        "phone_number": "1231231231",
        "api_token": "123testapitoken123",
        "first_name": "John",
        "last_name": "Doe",
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
    user = User.objects.create(**test_user_data)
    user.set_password(test_user_data["password"])
    user.set_basic_permissions()
    user.save()
    return user


@pytest.fixture
def client_with_jwt(test_user_data, test_user_instance):
    client_with_jwt = Client()
    auth_data = client_with_jwt.post(
        path=reverse("login"),
        data={
            "username": test_user_instance.username,
            "password": test_user_data["password"],
        },
    ).json()

    client_with_jwt.defaults["HTTP_AUTHORIZATION"] = f'Bearer {auth_data["access"]}'

    return client_with_jwt


@pytest.fixture
def admin_client_with_jwt(admin_user_credentials):
    user = User.objects.filter(username=admin_user_credentials["username"]).first()
    user.api_token = "api_token_test"
    user.save()

    admin_client_with_jwt = Client()
    auth_data = admin_client_with_jwt.post(path=reverse("login"), data=admin_user_credentials).json()

    admin_client_with_jwt.defaults["HTTP_AUTHORIZATION"] = f'Bearer {auth_data["access"]}'

    return admin_client_with_jwt
