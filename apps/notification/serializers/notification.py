from rest_framework import serializers

from apps.notification.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class NotificationReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    fid = serializers.CharField(read_only=True)
    rent = serializers.PrimaryKeyRelatedField(read_only=True)
    staff = serializers.PrimaryKeyRelatedField(read_only=True)
    type = serializers.CharField(read_only=True)
    status = serializers.BooleanField(read_only=True)
    content = serializers.CharField(read_only=True)
    hotel = serializers.PrimaryKeyRelatedField(read_only=True)
