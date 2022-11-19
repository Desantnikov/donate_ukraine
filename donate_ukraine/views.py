from rest_framework.viewsets import GenericViewSet

from donate_ukraine.mixins.views import (
    ListCreateRetrieveUpdateMixin,
    AuthenticationMixin,
)
from donate_ukraine.models import Lot, User
from donate_ukraine.serializers import LotSerializer, UserSerializer


class LotViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin, AuthenticationMixin):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer


class UserViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin, AuthenticationMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
