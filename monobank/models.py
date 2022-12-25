import datetime

from django.db import models
from django.utils.timezone import now


class MonobankJar(models.Model):
    title = models.CharField(max_length=40, default="")

    monobank_id = models.CharField(max_length=40, null=True)  # monobank id like `8OWpMMCU-Tfy11N7EF_mTcha66csZZE`
    link = models.CharField(max_length=40, default="")

    current_balance = models.IntegerField(default=0)
    highest_bid = models.IntegerField(default=0)

    last_updated = models.DateTimeField(default=now)
