from rest_framework import serializers

from apps.hotel.models import Hotel
from apps.room.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

    def validate(self, data):
        try:
            hotel = Hotel.objects.get(id=data['hotel'])
            if data['name'] in [room.name for room in hotel.rooms.all()]:
                raise Exception("Error")
        except Exception:
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
    services = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
