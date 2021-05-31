from rest_framework import serializers

from apps.rents.models import Rent


class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__'

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("Finish must occur after start")
        return data


class RentReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    fid = serializers.CharField(read_only=True)
    start_date = serializers.DateField(read_only=True)
    end_date = serializers.DateField(read_only=True)
    discount = serializers.IntegerField(read_only=True, min_value=0)
    totalAmount = serializers.IntegerField(read_only=True, min_value=0)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    details = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    feedback = serializers.PrimaryKeyRelatedField(read_only=True)
    status = serializers.BooleanField(read_only=True)
