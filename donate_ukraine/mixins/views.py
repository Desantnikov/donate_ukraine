from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ListCreateRetrieveUpdateMixin(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    pass


class AuthenticationMixin:
    permission_classes = [IsAuthenticatedOrReadOnly]
