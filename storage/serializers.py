import mimetypes

from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from storage.models import LotImage


class ImageSerializer(ModelSerializer):  # TODO: CHange name since all files are used now
    file_type = SerializerMethodField()

    class Meta:
        model = LotImage
        fields = "__all__"

    def get_file_type(self, obj):
        try:
            return mimetypes.guess_type(obj.file.name)[0]
        except:
            return "unknown"

    def validate(self, attrs):
        user = self.context["request"].user

        # ModelSerializer provides `lot_id` as Lot instance, not integer
        if attrs["lot_id"].creator == user:
            return super(ImageSerializer, self).validate(attrs)

        raise ValidationError({"user": "Only lot creator can have write access to photos"})
