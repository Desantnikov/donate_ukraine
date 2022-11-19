from rest_framework.serializers import ModelSerializer


from donate_ukraine.models import Lot, User


class LotSerializer(ModelSerializer):
    class Meta:
        model = Lot
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
