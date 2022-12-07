from rest_framework.viewsets import GenericViewSet
from rest_framework.serializers import ModelSerializer


from donate_ukraine.mixins.views import ListCreateRetrieveUpdateMixin
from storage.models import LotImage
from storage.serializers import ImageBase64Serializer


class LotImageViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin):
    view_permissions = {
        "list": {"admin": True, "user": True, "auctioneer": True},
        "create": {"admin": True, "user": True, "auctioneer": True},
        "retrieve": {"admin": True, "user": True, "auctioneer": True},
    }

    queryset = LotImage.objects.all()
    serializer_class = ImageBase64Serializer
