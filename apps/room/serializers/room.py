from rest_framework import serializers

from apps.room.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RoomReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    fid = serializers.CharField(read_only=True)
    hotel = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    price_now = serializers.IntegerField(read_only=True)
    status = serializers.BooleanField(read_only=True)
    image_url = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    adult = serializers.IntegerField(read_only=True)
    children = serializers.IntegerField(read_only=True)
    room_device = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    details = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
