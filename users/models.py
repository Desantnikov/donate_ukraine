from django.contrib.auth.models import (
    UserManager as DjangoUserManager,
    AbstractBaseUser,
    PermissionsMixin,
    AbstractUser,
)
from django.db import models

from mixins.models import ModeratableModelMixin


class UserManager(DjangoUserManager):
    def create_superuser(self, *args, **kwargs):
        user = super().create_superuser(role="admin", *args, **kwargs)

        return user


class User(AbstractUser, ModeratableModelMixin):
    REQUIRED_FIELDS = ["password", "api_token"]

    objects = UserManager()

    # to fetch data from auction creator's monobank jar
    api_token = models.CharField(max_length=60, null=False)  # encrypt
    role = models.CharField(max_length=20, default="user")

    phone_number = models.CharField(max_length=20, default="")  # needed for moderation
