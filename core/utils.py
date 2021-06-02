import pytz
from rest_framework import serializers

timezone = pytz.timezone('Asia/Ho_Chi_Minh')


def localize_datetime(datetime):
    return timezone.localize(datetime)


def create_model(data, Serializer):
    try:
        serializer = Serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer
    except Exception as e:
        raise Exception
