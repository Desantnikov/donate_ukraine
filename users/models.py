from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from fernet_fields import EncryptedTextField

from mixins.models import DeletableModelMixin, ModeratableModelMixin
from users.managers import UserManager
from users.permissions import BASIC_PERMISSIONS


class User(AbstractUser, ModeratableModelMixin, DeletableModelMixin):  #
    REQUIRED_FIELDS = ["first_name", "last_name", "password", "phone_number", "api_token"]

    objects = UserManager()

    # to fetch data from auction creator's monobank jar
    api_token = EncryptedTextField(blank=True, default="")  # encrypt

    phone_number = models.CharField(max_length=20, default="")  # needed for moderation

    def set_basic_permissions(self):
        permissions = Permission.objects.filter(
            codename__in=BASIC_PERMISSIONS,  # so user can add his monobank api key
        ).values_list(
            "id",
            flat=True,
        )
        self.user_permissions.add(*permissions)
