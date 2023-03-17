from django.db import models


class ModeratableModelMixin(models.Model):
    class Meta:
        abstract = True

    # TODO: set to False before deploys
    is_under_moderation = models.BooleanField(default=True)  # on create/edit


class DeletableModelMixin(models.Model):
    class Meta:
        abstract = True

    deleted_at = models.DateTimeField(null=True, default=None)
