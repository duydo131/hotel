from rest_framework import viewsets

from apps.room.filters import RoomDeviceFilterSet
from apps.room.models import RoomDevice
from apps.room.serializers.room_device import RoomDeviceSerializer, RoomDeviceReadOnlySerializer, \
    RoomDeviceDetailReadOnlySerializer
from core.mixins import GetSerializerClassMixin
from core.permissions import IsEmployee


class RoomDeviceViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsEmployee]

    queryset = RoomDevice.objects.filter()
    queryset_detail = RoomDevice.objects.prefetch_related('device')

    serializer_class = RoomDeviceSerializer
    serializer_detail_class = RoomDeviceDetailReadOnlySerializer

    serializer_action_classes = {
        "list": RoomDeviceReadOnlySerializer,
        "retrieve": RoomDeviceDetailReadOnlySerializer,
    }
    filterset_class = RoomDeviceFilterSet






