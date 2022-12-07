from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

from donate_ukraine.mixins.views import ListCreateRetrieveUpdateMixin
from donate_ukraine.models import Lot, User
from donate_ukraine.serializers import LotSerializer, UserSerializer


class LotViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Lot.objects.all()
    serializer_class = LotSerializer


class UserViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        User.objects.create_user(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
            email=serializer.validated_data["email"],
        )
        return Response("User created")


class UserInfoViewSet(GenericViewSet, RetrieveModelMixin):
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        print("USER INFO", flush=True)
        return self.request.user


class LogoutViewSet(GenericViewSet):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args):
        OutstandingToken.objects.filter(user=User.objects.first()).delete()

        return Response("Logged out")
