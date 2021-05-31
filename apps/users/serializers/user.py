from rest_framework import serializers

from apps.users.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["deleted", "password"]
        read_only_fields = ["created_at", "updated_at"]


class UserReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    fid = serializers.CharField(read_only=True)
    hotel = serializers.PrimaryKeyRelatedField(read_only=True)
    phone = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    address = serializers.CharField(read_only=True)
    avatar_url = serializers.CharField(read_only=True)
    gender = serializers.CharField(read_only=True)
    roles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    rents = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

