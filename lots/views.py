from rest_framework.viewsets import GenericViewSet

from mixins.views import ListCreateRetrieveUpdateMixin
from lots.models import Lot
from lots.serializers import LotCreateSerializer, LotDetailsSerializer, LotListSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.permissions import AllPermissionsSeparately


class LotListCreateRetrieveViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin):
    permission_classes = [IsAuthenticatedOrReadOnly | AllPermissionsSeparately]
    queryset = Lot.objects.filter(is_under_moderation=False)

    ACTION_TO_SERIALIZER_MAP = {
        "retrieve": LotDetailsSerializer,
        "list": LotListSerializer,
        "create": LotCreateSerializer,
    }

    def get_serializer_class(self):
        return self.ACTION_TO_SERIALIZER_MAP[self.action]
