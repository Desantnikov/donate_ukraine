from encodings.base64_codec import base64_encode
from rest_framework.response import Response

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
        "create": {"admin": True, "user": True, "auctioneer": True},
        "retrieve": {"admin": True, "user": True, "auctioneer": True},
    }

    queryset = LotImage.objects.all()
    serializer_class = LotImageSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        response_data = {
            "base64_encoded": base64_encode(instance.file.read()),
            "name": instance.name,
        }

        return Response(data=response_data)
