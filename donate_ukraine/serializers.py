from rest_framework import serializers

from donate_ukraine.models import Lot

class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = '__all__' #['id', 'account_name', 'users', 'created']