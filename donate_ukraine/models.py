from django.contrib.postgres.fields import ArrayField
from django.db import models

from monobank.models import MonobankJar
from users.models import User


class Lot(models.Model):
    creator = models.ForeignKey(User, models.PROTECT)

    name = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=512, default="")
    ending_date = models.DateTimeField(null=True)  # auction ends when jar is full or by ending date

    is_under_moderation = models.BooleanField(default=True)  # on create/edit

    # TODO: move report to separate model?
    report_text = models.CharField(max_length=512, default="")
    report_images = ArrayField(models.ImageField(upload_to="static"), default=list)

    monobank_jar = models.OneToOneField(MonobankJar, models.PROTECT, null=True)
