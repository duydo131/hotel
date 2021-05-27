from rest_framework import serializers

from apps.rents.models import RentDetail


class RentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentDetail
        fields = '__all__'


class RentDetailReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    fid = serializers.CharField(read_only=True)
    rent = serializers.PrimaryKeyRelatedField(read_only=True)
    room = serializers.PrimaryKeyRelatedField(read_only=True)
    price = serializers.IntegerField(read_only=True, min_value=0)
    voucher = serializers.FloatField(read_only=True, min_value=0)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
