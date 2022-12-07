from encodings.base64_codec import base64_encode

from rest_framework.serializers import ModelSerializer, SerializerMethodField

from storage.models import LotImage


class ImageBase64Serializer(ModelSerializer):
    class Meta:
        model = LotImage
        fields = "__all__"

    def to_representation(self, instance):
        response_data = {
            "base64_encoded": base64_encode(instance.file.read()),
            "name": instance.name,
        }

        return response_data


class ImageNameSerializer(ModelSerializer):
    class Meta:
        model = LotImage
        fields = "__all__"

    def to_representation(self, instance):
        return {"name": instance.name}
