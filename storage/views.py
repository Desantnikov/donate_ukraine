from rest_framework.viewsets import GenericViewSet
from rest_framework.serializers import ModelSerializer


from donate_ukraine.mixins.views import ListCreateRetrieveUpdateMixin
from storage.models import LotImage


class LotImageSerializer(ModelSerializer):
    class Meta:
        model = LotImage
        fields = "__all__"


class LotImageViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin):
    view_permissions = {
        "list": {"admin": True, "user": True, "auctioneer": True},
        "create": {"admin": True, "auctioneer": True},
        "retrieve": {"admin": True, "auctioneer": True},
    }

    queryset = LotImage.objects.all()
    serializer_class = LotImageSerializer
