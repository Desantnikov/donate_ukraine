# Create your views here.
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from mixins.views import ListCreateRetrieveUpdateMixin
from users.serializers import UserSerializer
from users.models import User


class UserViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin):  # TODO: remove list all users
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=["get"], detail=False, url_name="info", url_path="info", permission_classes=[IsAuthenticated])
    def info(self, request):
        serializer = self.get_serializer_class()(request.user)
        return Response(serializer.data)


class LogoutViewSet(GenericViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request, *args):
        refresh = RefreshToken.for_user(request.user)
        refresh.blacklist()
        return Response("Logged out")
