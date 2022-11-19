from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=254)


class Lot(models.Model):
    creator = models.ForeignKey(User, models.PROTECT)

    description = models.CharField(max_length=512, default="")
    photos = ArrayField(models.ImageField(), default=list)
    requisites = ArrayField(models.CharField(max_length=512, default=""), default=list)

    report_text = models.CharField(max_length=512, default="")
    report_images = ArrayField(models.ImageField(), default=list)
