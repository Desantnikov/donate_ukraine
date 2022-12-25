from rest_framework.serializers import ModelSerializer

from monobank.models import MonobankJar


class MonobankJarSerializer(ModelSerializer):
    class Meta:
        model = MonobankJar
        fields = "__all__"
