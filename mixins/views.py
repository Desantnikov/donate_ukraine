from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)


class AllActionsMixin(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    pass


class ListRetrieveMixin(ListModelMixin, RetrieveModelMixin):
    pass


class ListCreateRetrieveUpdateMixin(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    pass
