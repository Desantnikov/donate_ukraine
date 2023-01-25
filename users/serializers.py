import copy

from django.contrib.auth.models import Permission
from rest_framework.serializers import ModelSerializer

from lots.serializers import LotDetailsSerializer
from users.models import User


class UserSerializer(ModelSerializer):
    lots = LotDetailsSerializer(source="lot_set", many=True, required=False)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user_data = copy.copy(self.validated_data)

        # TODO: assign groups instead of permissions
        permissions = Permission.objects.filter(
            codename__in=["add_lot", "change_lot", "delete_lot"],
        ).values_list("id", flat=True)

        user = User.objects.create_user(**user_data)
        user.user_permissions.add(*permissions)

        return user

    # TODO: redeclare `edit` and `destroy` so it will be checking if it's their creator
