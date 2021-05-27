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
    name = serializers.CharField(read_only=True, validators=[UniqueValidator(queryset=Hotel.objects.all())])
    phone = serializers.CharField(read_only=True, validators=[UniqueValidator(queryset=Hotel.objects.all())])
    email = serializers.CharField(read_only=True, validators=[UniqueValidator(queryset=Hotel.objects.all())])
    fax = serializers.CharField(read_only=True, validators=[UniqueValidator(queryset=Hotel.objects.all())])
    address = serializers.CharField(read_only=True, validators=[UniqueValidator(queryset=Hotel.objects.all())])
    city = serializers.CharField(read_only=True)
    nation = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    stars = serializers.IntegerField(read_only=True)
    image_url = serializers.CharField(read_only=True)
    category = serializers.CharField(read_only=True)
    rating = RatingSerializer(read_only=True)
    rooms = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    feedbacks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
