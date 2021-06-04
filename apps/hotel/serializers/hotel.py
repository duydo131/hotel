from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.hotel.models import Hotel
from apps.hotel.serializers.rating import RatingSerializer


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"


class HotelReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    staff = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    fid = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    phone = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)
    fax = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    city = serializers.CharField(read_only=True)
    nation = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    stars = serializers.IntegerField(read_only=True)
    image_url = serializers.CharField(read_only=True)
    category = serializers.CharField(read_only=True)
    rating = RatingSerializer(read_only=True)
    score = serializers.FloatField(read_only=True, min_value=0)
    rooms = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    feedbacks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    total_room = serializers.IntegerField(read_only=True)
    turnove = serializers.IntegerField(read_only=True)


class StatisticalHotelReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    total_room = serializers.IntegerField(read_only=True)
    turnove = serializers.IntegerField(read_only=True)
    total_rent = serializers.IntegerField(read_only=True)
