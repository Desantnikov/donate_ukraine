from django.utils import timezone
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)


class AllActionsMixin(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    pass


class ListRetrieveMixin(ListModelMixin, RetrieveModelMixin):
    pass


class ListCreateRetrieveUpdateMixin(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    pass


class DeleteMixin(DestroyModelMixin):
    def perform_destroy(self, instance):
        instance.deleted_at = timezone.now()
        instance.save()
