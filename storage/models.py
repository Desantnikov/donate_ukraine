from django.db import models

from donate_ukraine.models import Lot


class LotImage(models.Model):
    name = models.CharField(max_length=50, default=None)
    file = models.ImageField(upload_to="media/images/lots", default=None)

    lot_id = models.ForeignKey(Lot, models.CASCADE)
