import copy

from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, ModelField, CharField, URLField

from donate_ukraine.models import Lot, User
from storage.serializers import ImageSerializer
from monobank.models import MonobankJar
from monobank.serializers import MonobankJarSerializer


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
    monobank_jar_title = CharField()  # should be a readonly=True, but they are not shown in api schema in that case
    monobank_jar_link = URLField()

    class Meta:
        model = Lot

        exclude = [
            "creator",  # creator (user) should be parsed from JWT token
            "monobank_jar",  # title and link instead
        ]

    def to_internal_value(self, data):
        monobank_jar = MonobankJar(
            title=data["monobank_jar_title"],
            link=data["monobank_jar_link"],
        )
        monobank_jar.save()

        data = super().to_internal_value(data)

        data["creator"] = self.context["request"].user
        data["monobank_jar"] = monobank_jar

        data.pop("monobank_jar_title")
        data.pop("monobank_jar_link")

        return data

    def create(self, validated_data):
        created_lot = super(LotCreateSerializer, self).create(validated_data)
        created_lot.monobank_jar.update_data()

        return created_lot

    def to_representation(self, instance):
        return {"id": instance.pk}


class UserSerializer(ModelSerializer):
    lots = LotDetailsSerializer(source="lot_set", many=True, required=False)

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
