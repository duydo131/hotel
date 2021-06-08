from uuid import UUID

from django.db.models import Q
from rest_framework import serializers

from apps.rents.models import RentDetail, Rent
from apps.room.models import Room
from core.utils import validate_positive


class RentDetailSerializer(serializers.ModelSerializer):

    def validate_price(self, value):
        return validate_positive(value, "price")

    def validate_voucher(self, value):
        return validate_positive(value, "voucher")

    def validate(self, data):
        try:
            rent = Rent.objects.get(id=data['rent'].id)
            room = Room.objects\
                .filter(id=data['room'].id)\
                .filter(Q(details__rent__status=True) & Q(details__rent__done=False))\
                .prefetch_related('details')\
                .first()
            if room is None:
                return data
            details = room.details.filter(Q(rent__status=True) & Q(rent__done=False))
            for detail in details:
                if not(rent.start_date >= detail.rent.end_date or rent.end_date <= detail.rent.start_date):
                    raise serializers.ValidationError("Room booked")
            return data
        except Exception as ex:
            raise serializers.ValidationError("Room booked")

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
