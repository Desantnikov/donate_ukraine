import pytest
from django.urls import reverse
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

from donate_ukraine.models import User


@pytest.mark.django_db
def test_create_user(client):
    user_data = {
        "username": "John",
        "password": "Doe",
        "email": "john@doe.com",
    }
    expected_response = {  # TODO: check why it returns so much fields while in postman only 4
        "password": "Doe",
        "last_login": None,
        "is_superuser": False,
        "username": "John",
        "email": "john@doe.com",
        "is_staff": False,
        "is_active": False,
        "groups": [],
        "user_permissions": [],
    }

    response = client.post(path=reverse("users"), data=user_data)

    User.objects.get(username="John", email="john@doe.com")

    assert response.status_code == 201
    assert response.json() == expected_response


@pytest.mark.django_db
def test_users_info(client, admin_user, admin_user_credentials):
    auth_data = client.post(path=reverse("login"), data=admin_user_credentials).json()

    client.defaults["HTTP_AUTHORIZATION"] = f'Bearer {auth_data["access"]}'

    response = client.get(path=reverse("users-info"))

    assert response.status_code == 200

    assert response.json()["username"] == "admin"
