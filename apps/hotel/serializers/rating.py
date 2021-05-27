from rest_framework import serializers

from apps.hotel.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class RatingReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    fid = serializers.CharField(read_only=True)
    comfortable = serializers.FloatField(read_only=True, min_value=0, max_value=10)
    address = serializers.FloatField(read_only=True, min_value=0, max_value=10)
    wifi_free = serializers.FloatField(read_only=True, min_value=0, max_value=10)
    staff = serializers.FloatField(read_only=True, min_value=0, max_value=10)
    convenirent = serializers.FloatField(read_only=True, min_value=0, max_value=10)
    clean = serializers.FloatField(read_only=True, min_value=0, max_value=10)
    hotel = serializers.PrimaryKeyRelatedField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

