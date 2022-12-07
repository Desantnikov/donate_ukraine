from rest_framework.viewsets import GenericViewSet
from rest_framework.serializers import ModelSerializer


from donate_ukraine.mixins.views import ListCreateRetrieveUpdateMixin
from storage.models import LotImage
from storage.serializers import ImageBase64Serializer, ImageNameSerializer


class LotImageViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin):
    view_permissions = {
        "list": {"admin": True, "user": True, "auctioneer": True},
        "create": {"admin": True, "user": True, "auctioneer": True},
        "retrieve": {"admin": True, "user": True, "auctioneer": True},
    }

    queryset = LotImage.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return ImageNameSerializer
        return ImageBase64Serializer
