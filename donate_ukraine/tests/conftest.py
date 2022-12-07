import pytest
from django.test import TestCase, RequestFactory


class UnitTest(TestCase):
    options = dict()

    def test_options(self, opts: dict):
        self.options = opts

    def test_data(self):
        self.setUpTestData()

    def request_factory(self):
        self.factory = RequestFactory()

    def setup(self, opts: dict):
        self.test_options(opts)
        self.test_data()
        self.request_factory()


@pytest.mark.django_db
class DatabaseTest:
    db = pytest.mark.django_db
    # def test_transaction(self):


async def django_db_setup(db):
    db()
    # settings.DATABASES["default"] = {
    #     "ENGINE": "django.db.backends.postgresql_psycopg2",
    #     "HOST": "example",
    #     "NAME": "test_db",
    #     "ATOMIC_REQUESTS": False,
    # }


@pytest.fixture
def admin_user_credentials(admin_user):
    return {"username": admin_user.username, "password": "password"}
