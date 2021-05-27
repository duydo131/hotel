from rest_framework import viewsets
from apps.room.filters import RoomFilterSet
from apps.room.models import Room
from apps.room.serializers import RoomSerializer, RoomReadOnlySerializer
from core.mixins import GetSerializerClassMixin
from core.permissions import IsEmployee


class RoomViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsEmployee]

    queryset = Room.objects.filter()

    serializer_class = RoomSerializer

    serializer_action_classes = {
        "list": RoomReadOnlySerializer,
        "retrieve": RoomReadOnlySerializer,
    }
    filterset_class = RoomFilterSet
