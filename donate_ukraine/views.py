from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

from donate_ukraine.mixins.views import ListCreateRetrieveUpdateMixin
from donate_ukraine.models import Lot, User
from donate_ukraine.serializers import LotSerializer, UserSerializer


class LotViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin):
    # permission_classes = [IsAuthenticatedOrReadOnly]

    view_permissions = {
        "list": {"admin": True, "user": True, "auctioneer": True},
        "create": {"admin": True, "auctioneer": True},
        "retrieve": {
            "admin": True,
            "auctioneer": True,
            "user": True,
        },
    }

    queryset = Lot.objects.all()
    serializer_class = LotSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     result = super().retrieve(request, *args, **kwargs)
    #
    #     return result


class UserViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin):
    permission_classes = [AllowAny]
    # view_permissions = {
    #     "list": {"admin": True, "user": False, "auctioneer": True},
    #     "retrieve": {"admin": True, "user": False, "auctioneer": True},
    #     "create": {"admin": True, "user": True, "auctioneer": True},
    # }

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
    # permission_classes = [IsAuthenticated]

    view_permissions = {
        "retrieve": {"admin": True, "user": True, "auctioneer": True},
    }

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class LogoutViewSet(GenericViewSet):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args):
        OutstandingToken.objects.filter(user=User.objects.first()).delete()

        return Response("Logged out")
