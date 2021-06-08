from rest_framework import serializers

from apps.room.models.service import Service
from core.utils import validate_positive


class ServiceSerializer(serializers.ModelSerializer):

    def validate_price(self, value):
        return validate_positive(value, "price")

    def validate_voucher(self, value):
        return validate_positive(value, "voucher")

    class Meta:
        model = Service
        fields = '__all__'


class ServiceReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    voucher = serializers.FloatField(read_only=True)
    description = serializers.CharField(read_only=True)
    room_categorys = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    rooms = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
