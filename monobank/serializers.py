from rest_framework.serializers import ModelSerializer, ReadOnlyField

from monobank.models import MonobankJar


class MonobankJarSerializer(ModelSerializer):
    link = ReadOnlyField()

    class Meta:
        model = MonobankJar
        fields = "__all__"
