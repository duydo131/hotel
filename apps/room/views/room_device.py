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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        room_device_id = dict(serializer.data)['id']
        room_device = RoomDevice.objects.get(id=room_device_id)
        if not room_device:
            raise APIException(
                _("Cannot create room device"),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        id_device = request.data['device']
        id_room = request.data['room']
        room = Room.objects.get(id=id_room)
        device = Device.objects.get(id=id_device)
        print(room)
        if not room and not device:
            raise APIException(
                _("Error Server"),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        room_device.room = room
        room_device.device = device
        room_device.save()
        serializer = RoomDeviceReadOnlySerializer(room_device)
        return Response(serializer.data, status=status.HTTP_201_CREATED)






