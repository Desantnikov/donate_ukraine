from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from mixins.views import DeleteMixin, ListCreateRetrieveUpdateMixin
from users.models import User
from users.permissions import AnyoneCanCreate
from users.serializers import UserSerializer


class UserViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin, DeleteMixin):  # TODO: remove list all users
    permission_classes = [AnyoneCanCreate]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=["get"], detail=False, url_name="info", url_path="info", permission_classes=[IsAuthenticated])
    def info(self, request):
        serializer = self.get_serializer_class()(request.user)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        if self.get_object() != self.request.user:
            raise PermissionDenied({"user": "You can't update another user's data"})

        return super(UserViewSet, self).update(request, *args, **kwargs)


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
