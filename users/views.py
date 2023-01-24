from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from mixins.views import ListCreateRetrieveUpdateMixin
from users.models import User
from users.serializers import LogoutSerializer, UserSerializer


class UserViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin):  # TODO: remove list all users
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=["get"], detail=False, url_name="info", url_path="info", permission_classes=[IsAuthenticated])
    def info(self, request):
        serializer = self.get_serializer_class()(request.user)
        return Response(serializer.data)


class LogoutViewSet(GenericViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = LogoutSerializer
    # def create(self, request, *args):
    #     refresh = RefreshToken.for_user(request.user)
    #     refresh.blacklist()
    #     return Response("Logged out")
