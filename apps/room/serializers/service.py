from rest_framework import serializers

from apps.room.models import Service


class ServiceSerializer(serializers.ModelSerializer):
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
