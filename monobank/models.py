from django.db import models


class MonobankJar(models.Model):
    jar_id = models.CharField(max_length=40)
    current_balance = models.IntegerField()
    highest_bid = models.IntegerField()

    last_updated = models.DateTimeField()
