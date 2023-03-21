from django.db import models

from lots.models import Lot


class LotImage(models.Model):  # TODO: CHange name since all files are used now
    # file = models.ImageField(upload_to="images/lots")
    file = models.FileField(upload_to="images/lots")  # FileField instead of ImageField to also accept videos and stuff

    lot_id = models.ForeignKey(Lot, models.CASCADE)
