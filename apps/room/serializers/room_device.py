from rest_framework import serializers

from apps.room.models import RoomDevice
from apps.room.serializers.device import DeviceReadOnlySerializer


class RoomDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomDevice
        fields = '__all__'


class RoomDeviceReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    fid = serializers.CharField(read_only=True)
    room = serializers.PrimaryKeyRelatedField(read_only=True)
    device = DeviceReadOnlySerializer(read_only=True)
    quantity = serializers.IntegerField(default=0)
