from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
from django.contrib.postgres.fields import ArrayField
from django.db import models

from monobank.models import MonobankJar


class UserManager(DjangoUserManager):
    def create_superuser(self, *args, **kwargs):
        user = super().create_superuser(role="admin", *args, **kwargs)

        return user


class User(AbstractUser):
    REQUIRED_FIELDS = ["password", "api_token"]

    objects = UserManager()

    # to fetch data from auction creator's monobank jar
    api_token = models.CharField(max_length=60, null=False)  # encrypt
    role = models.CharField(max_length=20, default="user")


class Lot(models.Model):
    creator = models.ForeignKey(User, models.PROTECT)

    name = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=512, default="")

    # TODO: remove field? all requisites stored in jar instance
    requisites = ArrayField(models.CharField(max_length=512, default=""), default=list)

    report_text = models.CharField(max_length=512, default="")
    report_images = ArrayField(models.ImageField(upload_to="static"), default=list)

    monobank_jar = models.OneToOneField(MonobankJar, models.PROTECT, null=True)  # TODO: make foreign key from Jar
