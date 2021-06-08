from rest_framework import serializers

from apps.users.models.user import User


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class RoleReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    fid = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    active = serializers.BooleanField(default=True)
