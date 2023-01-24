import json

import pytest
from django.db import connection
from django.test.client import Client
from django.urls import reverse

from users.models import User


@pytest.mark.django_db
def test_create_user(admin_client_with_jwt, test_user_data):
    initial_amount_of_users = User.objects.count()

    response = admin_client_with_jwt.post(
        path=reverse("users-list"), data=test_user_data, content_type="application/json"
    )

    users_queryset = User.objects.filter(username=test_user_data["username"], email=test_user_data["email"])

    assert response.status_code == 201
    assert users_queryset.exists()
    assert User.objects.count() == initial_amount_of_users + 1


@pytest.mark.django_db
def test_users_info(admin_client_with_jwt):
    response = admin_client_with_jwt.get(path=reverse("users-info"))

    assert response.status_code == 200
    assert response.json()["username"] == "admin"


@pytest.mark.django_db
def test_token_return(test_user_data):
    user = User.objects.create(**test_user_data)

    assert user.api_token == test_user_data["api_token"]


@pytest.mark.django_db
def test_token_encrypt(test_user_data):
    user = User.objects.create(**test_user_data)

    query_string = f"SELECT api_token FROM users_user WHERE username = '{test_user_data['username']}'"

    cursor = connection.cursor()
    cursor.execute(query_string)

    token = cursor.fetchone()[0]

    assert test_user_data["api_token"] != token
