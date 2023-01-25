from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError

from storage.models import LotImage


class ImageSerializer(ModelSerializer):
    class Meta:
        model = LotImage
        fields = "__all__"

    def validate(self, attrs):
        user = self.context["request"].user

        # ModelSerializer provides `lot_id` as Lot instance, not integer
        if attrs["lot_id"].creator == user:
            return super(ImageSerializer, self).validate(attrs)

        raise ValidationError({"user": "Only lot creator can have write access to photos"})
