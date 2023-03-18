import random
import string

from django.conf import settings
from django.core.mail import send_mail
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

    def destroy(self, request, *args, **kwargs):
        if request.user != self.get_object():
            raise PermissionDenied({"user": "You can't delete another user"})

        return super(UserViewSet, self).destroy(request, *args, **kwargs)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args):
        refresh = RefreshToken.for_user(request.user)
        refresh.blacklist()
        return Response("Logged out")


class RestorePasswordAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(status=404, data={"message": "Not found"})

        new_password = "".join(random.choice(string.ascii_lowercase) for _ in range(12))

        try:
            status = send_mail(
                subject="Password restoration",
                message=f"You have requested a password restoration. Your new password is: {new_password}",
                from_email="donate.ua.questions@gmail.com",
                recipient_list=[user.email],
                auth_user="apikey",
                auth_password=settings.MAIL_API_KEY,
            )
        except Exception as e:
            return Response(status=400, data={"message": f"Failed to send restore email with error: {e}"})

        if status != 1:
            return Response(status=400, data={"message": "Mail send status != 1"})

        user.set_password(new_password)
        user.save()

        return Response(status=200, data={"message": "Sent an email"})
