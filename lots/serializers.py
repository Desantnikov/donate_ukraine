import re

from rest_framework.exceptions import ValidationError
from rest_framework.serializers import CharField, ModelSerializer

from lots.models import Lot
from monobank.models import MonobankJar
from monobank.serializers import MonobankJarSerializer
from storage.serializers import ImageSerializer


class LotListRetrieveSerializer(ModelSerializer):
    photos = ImageSerializer(source="lotimage_set", many=True)
    monobank_jar = MonobankJarSerializer()

    class Meta:
        model = Lot
        fields = "__all__"


class LotCreateSerializer(ModelSerializer):
    monobank_jar_link = CharField()

    class Meta:
        model = Lot
        fields = ["name", "description", "winner_picking_type", "ending_date", "monobank_jar_link"]

    def validate(self, attrs):
        # TODO: make request to mono api to check if sendId/api-key are real
        if not self.context["request"].user.api_token:
            raise ValidationError({"api_token": "to create a lot you have to set your monobank api-token"})

        # TODO: validate that end-date is not earlier than now
        return super().validate(attrs)

    def to_internal_value(self, data):
        send_id = re.search(r"jar/\w{10}", data["monobank_jar_link"])
        if send_id is None:
            raise ValidationError({"monobank_jar_link": "Invalid - no sendId found"})

        monobank_jar = MonobankJar(send_id=send_id.group())
        monobank_jar.save()

        data = super().to_internal_value(data)

        data["creator"] = self.context["request"].user
        data["monobank_jar"] = monobank_jar

        data.pop("monobank_jar_link")

        return data

    def create(self, validated_data):
        created_lot = super(LotCreateSerializer, self).create(validated_data)
        created_lot.monobank_jar.update_data()

        return created_lot

    def to_representation(self, instance):
        return {"id": instance.pk}


class LotPartialUpdateSerializer(ModelSerializer):
    monobank_jar_link = CharField(required=False)

    class Meta:
        model = Lot
        # fields = "__all__"
        exclude = ("status",)

    # def validate(self, attrs):
    #     # TODO: make request to mono api to check if sendId/api-key are real
    #     return super().validate(attrs)
    #
    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
    #
    # def to_representation(self, instance):
    #     return {"id": instance.pk}
