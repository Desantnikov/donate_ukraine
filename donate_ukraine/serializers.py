from rest_framework.serializers import ModelSerializer

from donate_ukraine.models import Lot, User
from storage.views import ImageBase64Serializer


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

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #
    #     representation[]


class LotCreateSerializer(ModelSerializer):
    class Meta:
        model = Lot
        fields = "__all__"

    def to_representation(self, instance):
        return {"id": instance.pk}


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
