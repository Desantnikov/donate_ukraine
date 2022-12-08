from rest_framework.serializers import ModelSerializer

from donate_ukraine.models import Lot, User
from storage.serializers import ImageSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class LotDetailsSerializer(ModelSerializer):
    photos = ImageSerializer(source="lotimage_set", many=True)

    class Meta:
        model = Lot
        fields = "__all__"


class LotListSerializer(ModelSerializer):
    photo = ImageSerializer(source="lotimage_set.first", many=False)

    class Meta:
        model = Lot
        fields = "__all__"


class LotCreateSerializer(ModelSerializer):
    class Meta:
        model = Lot
        exclude = ["creator"]  # creator (user) should be parsed from JWT token

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        data["creator"] = self.context["request"].user
        return data

    def to_representation(self, instance):
        return {"id": instance.pk}
