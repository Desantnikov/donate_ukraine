from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import DestroyModelMixin
from rest_framework.response import Response
from django.db import transaction

from lots.models import Lot
from lots.serializers import LotCreateSerializer, LotListRetrieveSerializer, LotPartialUpdateSerializer
from mixins.views import ListCreateRetrieveUpdateMixin, ListRetrieveMixin
from users.permissions import AllPermissionsSeparately


class LotListCreateRetrieveUpdateViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin, DestroyModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly | AllPermissionsSeparately]
    queryset = Lot.objects.filter(is_under_moderation=False, is_active=True)

    ACTION_TO_SERIALIZER_MAP = {
        "retrieve": LotListRetrieveSerializer,
        "list": LotListRetrieveSerializer,
        "create": LotCreateSerializer,
        "partial_update": LotPartialUpdateSerializer,
        "update": LotCreateSerializer,
    }

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Lot.objects.filter(is_under_moderation=False,).order_by(
                "created_at",
            )

        # if authenticated - show lots as regular + lots created by user
        return Lot.objects.filter(is_under_moderation=False,) | Lot.objects.filter(creator=self.request.user).order_by(
            "created_at",
        )

    def get_serializer_class(self):
        return self.ACTION_TO_SERIALIZER_MAP[self.action]

    #  MonoJAR is created before creating a lot, so we have to rollback it in case user dont have an API_KEY
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        return super(LotListCreateRetrieveUpdateViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        is_creator = self.get_object().creator == request.user

        if not any([is_creator, request.user.is_superuser]):
            raise ValidationError({"user": "Only lot creator can modify it"})

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        lot = self.get_object()
        lot.is_under_moderation = True
        lot.save()
        return Response("sent for moderation")


class MyLotsListRetrieveUpdateViewSet(GenericViewSet, ListRetrieveMixin):
    permission_classes = [IsAuthenticatedOrReadOnly | AllPermissionsSeparately]
    serializer_class = LotListRetrieveSerializer
    # queryset = Lot.objects.all()

    def get_queryset(self):
        return Lot.objects.filter(creator=self.request.user)
