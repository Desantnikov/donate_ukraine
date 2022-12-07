from rest_framework.serializers import ModelSerializer

from donate_ukraine.models import Lot, User
from storage.serializers import ImageBase64Serializer


class LotDetailsSerializer(ModelSerializer):
    photos = ImageBase64Serializer(source="lotimage_set", many=True)

    class Meta:
        model = Lot
        fields = "__all__"


class LotsListSerializer(ModelSerializer):
    photo = ImageBase64Serializer(source="lotimage_set.first", many=False)

    class Meta:
        model = Lot
        fields = "__all__"


class LotCreateSerializer(ModelSerializer):
    class Meta:
        model = Lot
        exclude = ["creator"]

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        data["creator"] = self.context["request"].user
        return data

    def to_representation(self, instance):
        return {"id": instance.pk}


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
