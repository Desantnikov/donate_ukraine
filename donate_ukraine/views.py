from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoObjectPermissions
from rest_framework.viewsets import ViewSet, GenericViewSet

from mixins.views import ListCreateRetrieveUpdateMixin
from donate_ukraine.models import Lot
from donate_ukraine.serializers import LotCreateSerializer, LotDetailsSerializer, LotListSerializer


class No(DjangoModelPermissions):
    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }


class LotListRetrieveViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin):
    permission_classes = [No]
    queryset = Lot.objects.filter(is_under_moderation=False)

    ACTION_TO_SERIALIZER_MAP = {
        "retrieve": LotDetailsSerializer,
        "list": LotListSerializer,
        "create": LotCreateSerializer,
    }

    def get_serializer_class(self):
        return self.ACTION_TO_SERIALIZER_MAP[self.action]
