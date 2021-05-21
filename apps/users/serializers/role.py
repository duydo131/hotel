from rest_framework import serializers

from apps.users.models.user import User


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class RoleReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    fid = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(max_length=20, null=True, blank=True)
    active = serializers.BooleanField(default=True)
