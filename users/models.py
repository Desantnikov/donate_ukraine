from django.contrib.auth.models import UserManager as DjangoUserManager, AbstractUser
from django.db import models

from mixins.models import ModeratableModelMixin


class UserManager(DjangoUserManager):
    def create_superuser(self, *args, **kwargs):
        user = super().create_superuser(*args, **kwargs)

        return user


class User(AbstractUser, ModeratableModelMixin):
    REQUIRED_FIELDS = ["first_name", "last_name", "password", "phone_number", "api_token"]

    objects = UserManager()

    # to fetch data from auction creator's monobank jar
    api_token = models.CharField(max_length=60, null=False)  # encrypt

    phone_number = models.CharField(max_length=20, default="")  # needed for moderation
