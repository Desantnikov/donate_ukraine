from rest_framework.serializers import ModelSerializer

from storage.models import LotImage


class ImageSerializer(ModelSerializer):
    class Meta:
        model = LotImage
        fields = "__all__"
        # exclude = ["lot_id"]
