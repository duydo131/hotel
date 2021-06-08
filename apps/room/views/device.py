from rest_framework import viewsets

from apps.room.filters import DeviceFilterSet
from apps.room.models import Device
from apps.room.serializers.device import DeviceSerializer, DeviceReadOnlySerializer
from core.mixins import GetSerializerClassMixin
from core.permissions import IsEmployee


class DeviceViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsEmployee]

    queryset = Device.objects.filter()
    queryset_detail = Device.objects.filter()

    serializer_class = DeviceSerializer
    serializer_detail_class = DeviceReadOnlySerializer

    serializer_action_classes = {
        "list": DeviceReadOnlySerializer,
        "retrieve": DeviceReadOnlySerializer,
    }
    filterset_class = DeviceFilterSet






