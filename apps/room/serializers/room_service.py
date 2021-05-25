from rest_framework import serializers

from apps.room.models.room_service import RoomService


class RoomServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomService
        fields = '__all__'


class RoomServiceReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    services = serializers.PrimaryKeyRelatedField(many= True, read_only=True)
    room = serializers.PrimaryKeyRelatedField(read_only=True)
    rent = serializers.PrimaryKeyRelatedField(read_only=True)
