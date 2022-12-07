import pytest

# from donate_ukraine.models import User
from django.conf import settings


@pytest.mark.django_db
@pytest.fixture(autouse=True)
def django_db_setup():
    settings.DATABASES["default"] = {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": "example",
        "NAME": "test_db",
        "ATOMIC_REQUESTS": False,
    }


@pytest.fixture
def admin_user_credentials(admin_user):
    return {"username": admin_user.username, "password": "password"}
