from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from donate_ukraine.mixins.views import ListCreateRetrieveUpdateMixin
from donate_ukraine.models import Lot, User
from donate_ukraine.serializers import LotSerializer, UserSerializer


class LotViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Lot.objects.all()
    serializer_class = LotSerializer


class UserViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserInfoViewSet(GenericViewSet, RetrieveModelMixin):
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
