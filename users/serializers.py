import copy

from rest_framework.serializers import ModelSerializer

from donate_ukraine.serializers import LotDetailsSerializer
from users.models import User


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
