from rest_framework.viewsets import GenericViewSet

from donate_ukraine.mixins.views import AuthenticationMixin, ListCreateRetrieveUpdateMixin
from donate_ukraine.models import Lot, User
from donate_ukraine.serializers import LotSerializer, UserSerializer


class LotViewSet(AuthenticationMixin, GenericViewSet, ListCreateRetrieveUpdateMixin):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer


class UserViewSet(AuthenticationMixin, GenericViewSet, ListCreateRetrieveUpdateMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserTokenViewSet(AuthenticationMixin, GenericViewSet, ListCreateRetrieveUpdateMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return User.objects.first()
