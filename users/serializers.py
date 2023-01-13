import copy

from rest_framework.serializers import ModelSerializer

from lots.serializers import LotDetailsSerializer
from users.models import User


class UserSerializer(ModelSerializer):
    lots = LotDetailsSerializer(source="lot_set", many=True, required=False)

    class Meta:
        model = User
        fields = "__all__"

    def save(self, **kwargs):
        user_data = copy.copy(self.validated_data)

        user = User.objects.create_user(**user_data)

        return user
