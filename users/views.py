from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from users.permissions import AllPermissionsSeparately, AnyoneCanCreateOtherDepends

from mixins.views import ListCreateRetrieveUpdateMixin
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin):  # TODO: remove list all users
    permission_classes = [AnyoneCanCreateOtherDepends]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=["get"], detail=False, url_name="info", url_path="info", permission_classes=[IsAuthenticated])
    def info(self, request):
        serializer = self.get_serializer_class()(request.user)
        return Response(serializer.data)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args):
        refresh = RefreshToken.for_user(request.user)
        refresh.blacklist()
        return Response("Logged out")


# Maybe will be used one time
# class RestorePasswordAPIView(APIView):
#     permission_classes = [AllowAny]
#
#     parser_classes = [JSONParser]
#
#     def post(self, request, *args):
#         email = request.data.get('email')
#
#         user = User.objects.filter(email=email).first()
#
#         if user is None:
#             return Response(f"Email was sent to your address: {email}")
#
#
