from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, SerializerMethodField

from donate_ukraine.models import Lot, User
from storage.views import LotImageSerializer, ImageBase64Serializer


class LotShowSerializer(ModelSerializer):
    photos = ImageBase64Serializer(source="lotimage_set", many=True)

    class Meta:
        model = Lot
        fields = "__all__"


class LotCreateSerializer(ModelSerializer):
    class Meta:
        model = Lot
        fields = ["name", "description", "creator"]

    def to_representation(self, instance):
        return {"id": instance.pk}


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
