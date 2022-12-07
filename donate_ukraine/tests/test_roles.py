from rest_framework.test import APIRequestFactory

from donate_ukraine.models import User


factory = APIRequestFactory()


def create_user_test():
    return User.objects.create_user(username="test", role="test", email="test@test.com", password="test123")


def login_test():
    request = factory.post("/login", {"username": "root2", "password": "12345678"})
    return request
