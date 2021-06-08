from rest_framework import serializers
from rest_framework.utils import model_meta

from apps.room.models import Room
from apps.room.serializers.service import ServiceReadOnlySerializer


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

    def validate_name(self, name):
        if self.instance and Room.objects.filter(hotel_id=self.instance.hotel_id, name=name).exists():
            raise serializers.ValidationError("Room name in hotel is unique")
        return name

    def validate(self, data):
        hotel = data.get('hotel')
        if not self.instance and data.get("name", None) and Room.objects.filter(hotel=hotel, name=data["name"]):
            raise serializers.ValidationError("Room name in hotel is unique")

        return data


class RoomReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    fid = serializers.CharField(read_only=True)
    hotel = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(read_only=True)
    price = serializers.IntegerField(read_only=True, min_value=0)
    price_now = serializers.IntegerField(read_only=True, min_value=0)
    status = serializers.BooleanField(read_only=True)
    image_url = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    adult = serializers.IntegerField(read_only=True, min_value=1)
    children = serializers.IntegerField(read_only=True, min_value=0)
    room_device = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    details = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


class RoomDetailReadOnlySerializer(RoomReadOnlySerializer):
    services = ServiceReadOnlySerializer(many=True, read_only=True)
