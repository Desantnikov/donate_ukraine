import pytest
from django.urls import reverse

from users.models import User


@pytest.mark.django_db
def test_create_user(client):
    user_data = {
        "username": "John",
        "password": "Doe",
        "email": "john@doe.com",
        "api_token": "asdasd",
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
        "api_token": "asdasd",
    }
    response = client.post(path=reverse("users-list"), data=user_data)

    User.objects.get(username="John", email="john@doe.com")

    assert response.status_code == 201
    assert response.json() == expected_response


@pytest.mark.django_db
def test_users_info(admin_client_with_jwt):
    response = admin_client_with_jwt.get(path=reverse("users-info"))

    assert response.status_code == 200
    assert response.json()["username"] == "admin"
