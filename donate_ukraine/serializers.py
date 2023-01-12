import copy

from rest_framework.serializers import ModelSerializer

from donate_ukraine.models import Lot, User
from storage.serializers import ImageSerializer
from monobank.models import MonobankJar
from monobank.serializers import MonobankJarSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def save(self, **kwargs):
        user_data = copy.copy(self.validated_data)

        # m2m fields can't be set during creation
        groups = user_data.pop("groups", [])
        user_permissions = user_data.pop("user_permissions", [])

        user = User.objects.create_user(**user_data)
        user.groups.set(groups)
        user.user_permissions.set(user_permissions)

        return user


class LotDetailsSerializer(ModelSerializer):
    photos = ImageSerializer(source="lotimage_set", many=True)
    monobank_jar = MonobankJarSerializer()

    class Meta:
        model = Lot
        fields = "__all__"


class LotListSerializer(ModelSerializer):
    photo = ImageSerializer(source="lotimage_set.first", many=False)
    monobank_jar = MonobankJarSerializer()

    class Meta:
        model = Lot
        fields = "__all__"


class LotCreateSerializer(ModelSerializer):
    class Meta:
        model = Lot
        exclude = ["creator"]  # creator (user) should be parsed from JWT token

    def to_internal_value(self, data):
        monobank_jar = MonobankJar(
            title=data["monobank_jar_title"],
            link=data["link_to_monobank_jar"],
        )
        monobank_jar.save()

        data = super().to_internal_value(data)

        data["creator"] = self.context["request"].user
        data["monobank_jar"] = monobank_jar

        return data

    def create(self, validated_data):
        created_lot = super(LotCreateSerializer, self).create(validated_data)
        created_lot.monobank_jar.update_data()

        return created_lot

    def to_representation(self, instance):
        return {"id": instance.pk}
