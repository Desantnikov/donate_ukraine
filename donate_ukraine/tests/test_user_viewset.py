import pytest_django.fixtures
from django.urls import reverse
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
import pytest

# TODO: initialize new test DB instead of using existing


@pytest.mark.django_db
def test_login_endpoint_returns_two_tokens(client, admin_user, admin_user_credentials):
    response_data = client.post(
        path=reverse("login"),
        data=admin_user_credentials,
    ).json()

    assert set(response_data.keys()) == {"access", "refresh"}


@pytest.mark.django_db
def test_login_endpoint_creates_token_in_db(client, admin_user, admin_user_credentials):
    tokens_amount_before_login = OutstandingToken.objects.all().count()

    client.post(path=reverse("login"), data=admin_user_credentials)

    assert OutstandingToken.objects.all().count() == tokens_amount_before_login + 1


# TODO: finish
# def test_logout(client, admin_user, admin_user_credentials):
#     tokens_amount_before_logout = OutstandingToken.objects.all().count()
#
#     client.post(path=reverse('logout'))
#
#     assert OutstandingToken.objects.all().count() == tokens_amount_before_logout - 1
