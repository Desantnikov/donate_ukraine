from django.db import models

from lots.models import Lot


class LotImage(models.Model):
    file = models.ImageField(upload_to="images/lots")

    lot_id = models.ForeignKey(Lot, models.CASCADE)
