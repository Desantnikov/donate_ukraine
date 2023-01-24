from rest_framework.serializers import ModelSerializer, ReadOnlyField

from monobank.models import MonobankJar


class MonobankJarSerializer(ModelSerializer):
    link = ReadOnlyField()

    class Meta:
        model = MonobankJar
        fields = "__all__"

        cash_fields = ["current_balance", "goal", "highest_bid"]  # TODO: move to mixin?

    def to_representation(self, instance):
        representation = super(MonobankJarSerializer, self).to_representation(instance)

        for field_name in MonobankJarSerializer.Meta.cash_fields:  # TODO: refactor
            representation[field_name] = self.remove_coins(representation[field_name])

        return representation

    @staticmethod
    def remove_coins(cash_amount):
        return int(cash_amount / 100)
