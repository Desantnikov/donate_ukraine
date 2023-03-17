from django.contrib.postgres.fields import ArrayField
from django.db import models

from lots.managers import LotManager
from mixins.models import DeletableModelMixin
from lots.constants import LOT_STATUS
from monobank.models import MonobankJar
from users.models import User


class Lot(DeletableModelMixin):
    class Meta:
        default_permissions = ("add", "change", "delete")
        permissions = (("view_post", "Can view post"),)
        get_latest_by = "-created_at"
        ordering = ("-created_at",)

    objects = LotManager()

    creator = models.ForeignKey(User, models.PROTECT)
    name = models.CharField(max_length=100, default="", unique=True)
    description = models.CharField(max_length=2048, default="")
    ending_date = models.DateTimeField(null=True)  # auction ends when jar is full or by ending date
    monobank_jar = models.OneToOneField(MonobankJar, on_delete=models.PROTECT, null=True)

    status = models.CharField(choices=LOT_STATUS.values(), default=LOT_STATUS.MODERATION, max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    # TODO: move report to separate model?
    report_text = models.CharField(max_length=512, default="", blank=True)
    report_images = ArrayField(models.ImageField(upload_to="static"), default=list, blank=True)
