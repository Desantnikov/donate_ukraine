import pytest
from django.db import connection

from users.models import User


@pytest.mark.django_db
def test_token_return(test_user_data):
    user = User.objects.create(**test_user_data)

    assert user.api_token == test_user_data["api_token"]


@pytest.mark.django_db
def test_token_encrypt(test_user_instance):
    query_string = f"SELECT api_token FROM users_user WHERE username = '{test_user_instance.username}'"

    cursor = connection.cursor()
    cursor.execute(query_string)

    token = cursor.fetchone()[0]

    assert test_user_instance.api_token != token
