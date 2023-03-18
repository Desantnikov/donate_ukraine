import copy

from django.contrib.auth.models import Permission
from rest_framework.serializers import ModelSerializer

from lots.serializers import LotListRetrieveSerializer
from users.models import User


class UserSerializer(ModelSerializer):
    lots = LotListRetrieveSerializer(source="lot_set", many=True, required=False)

    class Meta:
        model = User
        # TODO: don't show api token to user
        fields = ("first_name", "last_name", "username", "email", "phone_number", "api_token", "lots")

    def create(self, validated_data):
        user_data = copy.copy(self.validated_data)

        user = User.objects.create_user(**user_data)
        user.set_basic_permissions()

        return user

    # TODO: redeclare `edit` and `destroy` so it will be checking if it's their creator
