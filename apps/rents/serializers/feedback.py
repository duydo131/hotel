from rest_framework import serializers

from apps.rents.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class FeedbackReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    fid = serializers.CharField(read_only=True)
    comfortable = serializers.IntegerField(read_only=True, min_value=0, max_value=10)
    address = serializers.IntegerField(read_only=True, min_value=0, max_value=10)
    wifi_free = serializers.IntegerField(read_only=True, min_value=0, max_value=10)
    staff = serializers.IntegerField(read_only=True, min_value=0, max_value=10)
    convenirent = serializers.IntegerField(read_only=True, min_value=0, max_value=10)
    clean = serializers.IntegerField(read_only=True, min_value=0, max_value=10)
    content = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    rent = serializers.PrimaryKeyRelatedField(read_only=True)
    hotel = serializers.PrimaryKeyRelatedField(read_only=True)
