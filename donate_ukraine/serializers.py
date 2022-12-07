from rest_framework.serializers import ModelSerializer

from donate_ukraine.models import Lot, User
from storage.views import LotImageSerializer, ImageBase64Serializer


class LotSerializer(ModelSerializer):
    photos = ImageBase64Serializer(source="lotimage_set", many=True)

    class Meta:
        model = Lot
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
