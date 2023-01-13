from rest_framework.serializers import ModelSerializer, CharField, URLField, ValidationError

from lots.models import Lot
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
    monobank_jar_title = CharField()
    monobank_jar_link = URLField()

    class Meta:
        model = Lot
        fields = ["name", "description", "ending_date", "monobank_jar_title", "monobank_jar_link"]

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