from rest_framework import serializers

from apps.rents.models import Feedback
from core.utils import invalidRating


class FeedbackSerializer(serializers.ModelSerializer):
    def validate_comfortable(self, value):
        return invalidRating(value, "comfortable")

    def validate_address(self, value):
        return invalidRating(value, "address")

    def validate_wifi_free(self, value):
        return invalidRating(value, "wifi_free")

    def validate_staff(self, value):
        return invalidRating(value, "staff")

    def validate_convenirent(self, value):
        return invalidRating(value, "convenirent")

    def validate_clean(self, value):
        return invalidRating(value, "clean")

    class Meta:
        model = Feedback
        fields = '__all__'


class FeedbackReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    fid = serializers.CharField(read_only=True)
    comfortable = serializers.IntegerField(read_only=True)
    address = serializers.IntegerField(read_only=True)
    wifi_free = serializers.IntegerField(read_only=True)
    staff = serializers.IntegerField(read_only=True)
    convenirent = serializers.IntegerField(read_only=True)
    clean = serializers.IntegerField(read_only=True)
    content = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    rent = serializers.PrimaryKeyRelatedField(read_only=True)
    hotel = serializers.PrimaryKeyRelatedField(read_only=True)
