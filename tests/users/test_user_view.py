import pytest
from django.urls import reverse

from users.models import User
from users.permissions import BASIC_PERMISSIONS


@pytest.mark.django_db
def test_create_user(client, test_user_data):
    initial_amount_of_users = User.objects.count()

    response = client.post(path=reverse("users-list"), data=test_user_data)
    assert response.status_code == 201

    users_queryset = User.objects.filter(
        username=test_user_data["username"],
        email=test_user_data["email"],
    )

    assert users_queryset.exists()
    assert User.objects.count() == initial_amount_of_users + 1


@pytest.mark.django_db
def test_created_user_has_basic_permissions(client, test_user_data):
    response = client.post(path=reverse("users-list"), data=test_user_data, content_type="application/json")
    assert response.status_code == 201

    user = User.objects.get(username=test_user_data["username"])

    user_permissions_codenames = set(permission.codename for permission in user.user_permissions.all())

    assert user_permissions_codenames == set(BASIC_PERMISSIONS)


@pytest.mark.django_db
def test_user_edit_data(client_with_jwt, test_user_data, updated_test_user_data):
    response = client_with_jwt.get(path=reverse("users-info"))

    assert response.status_code == 200
    assert response.json()["api_token"] == test_user_data["api_token"]

    user_id = User.objects.get(username=test_user_data["username"]).id

    client_with_jwt.patch(
        path=f"/users/{user_id}",
        data=updated_test_user_data,
        content_type="application/json",
    )

    response = client_with_jwt.get(path=reverse("users-info"))

    assert response.status_code == 200
    assert response.json()["api_token"] == updated_test_user_data["api_token"]
    assert response.json()["email"] == updated_test_user_data["email"]


@pytest.mark.django_db
def test_exception_on_changing_another_user_data(
    client_with_jwt, admin_client_with_jwt, test_user_data, updated_test_user_data, secondary_test_user_instance
):
    response = client_with_jwt.patch(
        path=f"/users/{secondary_test_user_instance.id}",
        data=updated_test_user_data,
        content_type="application/json",
    )

    assert response.status_code == 403
    assert response.json() == {"user": "You can't update another user's data"}


@pytest.mark.django_db
def test_users_info_returns_data_when_authorized(admin_client_with_jwt, admin_user_credentials):
    response = admin_client_with_jwt.get(path=reverse("users-info"))

    assert response.status_code == 200
    assert response.json()["username"] == admin_user_credentials["username"]
    assert response.json()["lots"] == []


@pytest.mark.django_db
def test_get_users_info_returns_error_when_not_authorized(client):
    response = client.get(path=reverse("users-info"))

    assert response.status_code == 401
    assert response.json() == {"detail": "Authentication credentials were not provided."}


#
# @pytest.mark.django_db
# def test_qweqwe(client):
#     breakpoint()
#     response = client.get(path=reverse("users-info"))
#
#     assert response.status_code == 401
#     assert response.json() == {'detail': 'Authentication credentials were not provided.'}
