from rest_framework import viewsets

from apps.room.filters import RoomDeviceFilterSet
from apps.room.models import Room, RoomDevice, Device
from apps.room.serializers.room_device import RoomDeviceSerializer, RoomDeviceReadOnlySerializer
from core.mixins import GetSerializerClassMixin
from core.permissions import IsEmployee
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.response import Response


class RoomDeviceViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsEmployee]

    queryset = RoomDevice.objects.filter()

    serializer_class = RoomDeviceSerializer

    serializer_action_classes = {
        "list": RoomDeviceReadOnlySerializer,
        "retrieve": RoomDeviceReadOnlySerializer,
    }
    filterset_class = RoomDeviceFilterSet






