from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet
from django.db import transaction

from lots.models import Lot
from lots.serializers import LotCreateSerializer, LotDetailsSerializer, LotListSerializer, LotPartialUpdateSerializer
from mixins.views import ListCreateRetrieveUpdateMixin
from users.permissions import AllPermissionsSeparately


class LotListCreateRetrieveUpdateViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin):
    permission_classes = [IsAuthenticatedOrReadOnly | AllPermissionsSeparately]
    queryset = Lot.objects.filter()

    ACTION_TO_SERIALIZER_MAP = {
        "retrieve": LotDetailsSerializer,
        "list": LotListSerializer,
        "create": LotCreateSerializer,
        "partial_update": LotPartialUpdateSerializer,
        "update": LotCreateSerializer,
    }

    def get_serializer_class(self):
        return self.ACTION_TO_SERIALIZER_MAP[self.action]

    #  MonoJAR is created before creating a lot, so we have to rollback it in case user dont have an API_KEY
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        return super(LotListCreateRetrieveUpdateViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        is_creator = self.get_object().creator == request.user

        if not any([is_creator, request.user.is_superuser]):
            raise ValidationError({"user": "Only lot creator can modify it"})

        return super().update(request, *args, **kwargs)
