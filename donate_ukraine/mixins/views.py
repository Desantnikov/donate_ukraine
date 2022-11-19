from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)


class ListCreateRetrieveUpdateMixin(
    ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
):
    pass


class AuthenticationMixin:
    pass
