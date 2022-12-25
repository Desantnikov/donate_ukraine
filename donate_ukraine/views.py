from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

from donate_ukraine.mixins.views import ListCreateRetrieveUpdateMixin
from donate_ukraine.models import Lot, User
from donate_ukraine.serializers import LotCreateSerializer, LotDetailsSerializer, LotListSerializer, UserSerializer


class LotViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin):
    permission_classes = [IsAuthenticated]

    queryset = Lot.objects.all()

    ACTION_TO_SERIALIZER_MAP = {
        "retrieve": LotDetailsSerializer,
        "list": LotListSerializer,
        "create": LotCreateSerializer,
    }

    def get_serializer_class(self):
        return self.ACTION_TO_SERIALIZER_MAP[self.action]


class UserViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=["get"], detail=False, url_name="info", url_path="info", permission_classes=[IsAuthenticated])
    def info(self, request):
        serializer = self.get_serializer_class()(request.user)
        return Response(serializer.data)


class LogoutViewSet(GenericViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request, *args):  # TODO: rename method
        OutstandingToken.objects.filter(user=self.request.user).delete()  # TODO: FIx this w/a
        return Response("Logged out")
