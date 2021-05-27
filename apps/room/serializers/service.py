from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.room.models.service import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True, validators=[UniqueValidator(queryset=Service.objects.all())])
    price = serializers.IntegerField(read_only=True, min_value=0)
    voucher = serializers.FloatField(read_only=True, min_value=0)
    description = serializers.CharField(read_only=True)
    room_categorys = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    rooms = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
