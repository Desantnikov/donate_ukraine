from django.db import transaction
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import DestroyModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from lots.models import Lot
from lots.serializers import LotCreateSerializer, LotListRetrieveSerializer, LotPartialUpdateSerializer
from mixins.views import DeleteMixin, ListCreateRetrieveUpdateMixin, ListRetrieveMixin
from users.permissions import AllPermissionsSeparately


class LotAllActionsViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin, DeleteMixin):
    permission_classes = [IsAuthenticatedOrReadOnly | AllPermissionsSeparately]  # TODO: permissions are not safe
    queryset = Lot.objects.filter()

    ACTION_TO_SERIALIZER_MAP = {
        "retrieve": LotListRetrieveSerializer,
        "list": LotListRetrieveSerializer,
        "create": LotCreateSerializer,
        "partial_update": LotPartialUpdateSerializer,
        "update": LotCreateSerializer,
    }

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Lot.objects.without_moderation()

        # if authenticated - show lots as regular + lots created by user
        return Lot.objects.without_moderation() | Lot.objects.created_by(self.request.user)

    def get_serializer_class(self):
        return self.ACTION_TO_SERIALIZER_MAP[self.action]

    #  MonoJAR is created before creating a lot, so we have to rollback it in case user dont have an API_KEY
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        return super(LotAllActionsViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        is_creator = self.get_object().creator == request.user

        if not any([is_creator, request.user.is_superuser]):
            raise ValidationError({"user": "Only lot creator can modify it"})

        if request.data.get("status") is not None:
            raise ValidationError({"user": "Only admin can change status"})

        return super().update(request, *args, **kwargs)


# returns lots owned by specific (request) user
class MyLotsListRetrieveUpdateViewSet(GenericViewSet, ListRetrieveMixin):
    permission_classes = [IsAuthenticatedOrReadOnly | AllPermissionsSeparately]
    serializer_class = LotListRetrieveSerializer
    # queryset = Lot.objects.all()

    def get_queryset(self):
        return Lot.objects.filter(creator=self.request.user)
