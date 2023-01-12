from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin


class ListCreateRetrieveUpdateMixin(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    pass
