from rest_framework import serializers

from apps.hotel.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class RatingReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    fid = serializers.CharField(read_only=True)
    comfortable = serializers.FloatField(read_only=True)
    address = serializers.FloatField(read_only=True)
    wifi_free = serializers.FloatField(read_only=True)
    staff = serializers.FloatField(read_only=True)
    convenirent = serializers.FloatField(read_only=True)
    clean = serializers.FloatField(read_only=True)
    hotel = serializers.PrimaryKeyRelatedField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
