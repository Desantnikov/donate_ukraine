from django.db import models

from lots.constants import LOT_STATUS


class LotManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

    def without_moderation(self):
        return self.exclude(status=LOT_STATUS.MODERATION)

    def active(self):
        return self.filter(status=LOT_STATUS.ACTIVE)

    def created_by(self, user):
        return self.filter(creator=user)

    def with_deleted(self):
        return super().get_queryset()
