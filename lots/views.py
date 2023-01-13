from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import ValidationError

from mixins.views import ListCreateRetrieveUpdateMixin
from lots.models import Lot
from lots.serializers import LotCreateSerializer, LotDetailsSerializer, LotListSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.permissions import AllPermissionsSeparately


class LotListCreateRetrieveUpdateViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin):
    permission_classes = [IsAuthenticatedOrReadOnly | AllPermissionsSeparately]
    queryset = Lot.objects.filter()

    ACTION_TO_SERIALIZER_MAP = {
        "retrieve": LotDetailsSerializer,
        "list": LotListSerializer,
        "create": LotCreateSerializer,
        "partial_update": LotCreateSerializer,
    }

    def get_serializer_class(self):
        return self.ACTION_TO_SERIALIZER_MAP[self.action]

    def update(self, request, *args, **kwargs):
        is_creator = self.get_object().creator == request.user

        if not any([is_creator, request.user.is_superuser]):
            raise ValidationError("Only lot creator can modify it")

        return super().update(request, *args, **kwargs)
