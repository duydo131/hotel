import datetime

from rest_framework import serializers

from apps.rents.models import Rent
from apps.rents.serializers.rent_detail import RentDetailReadOnlySerializer
from core.utils import validate_positive


def validate_start_end_date(start, end):
    if start > end:
        raise serializers.ValidationError("End date must occur after start date")


def validate_start_date(start, today):
    if start < today:
        raise serializers.ValidationError("Start date must occur after today")


class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__'

    def validate_discount(self, value):
        return validate_positive(value, "discount")

    def validate_total_amount(self, value):
        return validate_positive(value, "total amount")

    def validate(self, data):
        if self.instance:
            validate_start_end_date(data.get('start_date', self.instance.start_date), data.get('end_date', self.instance.end_date))
            validate_start_date(data.get('start_date', self.instance.start_date), datetime.date.today())
            return data

        validate_start_end_date(data['start_date'], data['end_date'])
        validate_start_date(data['end_date'], datetime.date.today())
        return data


class RentReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    fid = serializers.CharField(read_only=True)
    start_date = serializers.DateField(read_only=True)
    end_date = serializers.DateField(read_only=True)
    discount = serializers.IntegerField(read_only=True)
    total_amount = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    details = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    feedback = serializers.PrimaryKeyRelatedField(read_only=True)
    status = serializers.BooleanField(read_only=True)
    done = serializers.BooleanField(read_only=True)
    hotel = serializers.PrimaryKeyRelatedField(read_only=True)


class RentGetDetailReadOnlySerializer(RentReadOnlySerializer):
    details = RentDetailReadOnlySerializer(many=True, read_only=True)