from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager


class User(AbstractUser):
    email = models.EmailField(max_length=254)


class Lot(models.Model):
    creator = models.ForeignKey(User, models.PROTECT)

    description = models.CharField(max_length=512, default='')
    photos = models.CharField(max_length=100, default='')
    requisites = models.CharField(max_length=512, default='')

    report_text = models.CharField(max_length=512, default='')
    report_images = models.CharField(max_length=100, default='')
