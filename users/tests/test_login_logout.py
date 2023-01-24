import pytest
from django.urls import reverse
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken


@pytest.mark.django_db
def test_login_endpoint_returns_two_tokens(client, admin_user, admin_user_credentials):
    response_data = client.post(path=reverse("login-list"), data=admin_user_credentials).json()

    assert set(response_data.keys()) == {"access", "refresh"}


@pytest.mark.django_db
def test_login_endpoint_creates_token_in_db(client, admin_user, admin_user_credentials):
    tokens_amount_before_login = OutstandingToken.objects.all().count()

    client.post(path=reverse("login-list"), data=admin_user_credentials)

    assert OutstandingToken.objects.all().count() == tokens_amount_before_login + 1


@pytest.mark.django_db
def test_token_deleted_after_logout(client, admin_user, admin_user_credentials):
    blacklisted_tokens_amount = BlacklistedToken.objects.all().count()

    response_data = client.post(path=reverse("login-list"), data=admin_user_credentials).json()

    client.defaults["HTTP_AUTHORIZATION"] = f'Bearer {response_data["access"]}'
    client.post(path=reverse("logout-list"))

    assert BlacklistedToken.objects.all().count() == blacklisted_tokens_amount + 1


@pytest.mark.django_db
def test_login_error_on_wrong_credentials(client, admin_user, admin_user_credentials):
    response = client.post(
        path=reverse("login-list"),
        data={
            "username": "non-existent",
            "password": "blabla",
        },
    )

    assert response.status_code == 401
    assert response.json() == {"detail": "No active account found with the given credentials"}
