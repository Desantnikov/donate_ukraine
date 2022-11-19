from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    pass


class Lot(models.Model):
    creator = models.ForeignKey(User, models.PROTECT)

    name = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=512, default="")
    photos = ArrayField(models.ImageField(upload_to="static"), default=list)
    requisites = ArrayField(models.CharField(max_length=512, default=""), default=list)

    report_text = models.CharField(max_length=512, default="")
    report_images = ArrayField(models.ImageField(upload_to="static"), default=list)
