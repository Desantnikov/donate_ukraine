from django.contrib.postgres.fields import ArrayField
from django.db import models

from mixins.models import ModeratableModelMixin
from monobank.models import MonobankJar
from users.models import User


class Lot(ModeratableModelMixin):
    class Meta:
        default_permissions = ("add", "change", "delete")
        permissions = (("view_post", "Can view post"),)
        get_latest_by = "created_at"

    creator = models.ForeignKey(User, models.PROTECT)

    name = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=512, default="")
    ending_date = models.DateTimeField(null=True)  # auction ends when jar is full or by ending date
    monobank_jar = models.OneToOneField(MonobankJar, models.PROTECT, null=True)

    is_active = models.BooleanField(default=True)

    # date_created = models.DateTimeField(default=django.utils.timezone.now)

    # TODO: move report to separate model?
    report_text = models.CharField(max_length=512, default="", blank=True)
    report_images = ArrayField(models.ImageField(upload_to="static"), default=list, blank=True)
