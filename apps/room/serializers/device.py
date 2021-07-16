from rest_framework import serializers

from apps.room.models import Device
from core.utils import validate_positive


class DeviceSerializer(serializers.ModelSerializer):

    def validate_price(self, value):
        return validate_positive(value, "price")

    class Meta:
        model = Device
        fields = '__all__'


class DeviceReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    fid = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    price = serializers.IntegerField(read_only=True, min_value=0)
    image_url = serializers.CharField(read_only=True)


class DeviceReadXXXOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    fid = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    image_url = serializers.CharField(read_only=True)
    room_device = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
