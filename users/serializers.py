from rest_framework.serializers import ModelSerializer

from lots.serializers import LotListRetrieveSerializer
from users.models import User


class UserSerializer(ModelSerializer):
    lots = LotListRetrieveSerializer(source="lot_set", many=True, required=False)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password", "phone_number", "api_token", "lots")

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_basic_permissions()

        return user

    def to_representation(self, instance):
        user_dict = super().to_representation(instance)
        user_dict.pop("password")
        user_dict["id"] = instance.id

        return user_dict

    # TODO: redeclare `edit` and `destroy` so it will be checking if it's their creator
