from rest_framework import viewsets

from apps.hotel.models import Hotel
from apps.room.filters import RoomFilterSet
from apps.room.models import Room, RoomCategory
from apps.room.serializers import RoomSerializer, RoomReadOnlySerializer
from core.mixins import GetSerializerClassMixin
from core.permissions import IsAdmin, IsEmployee
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.response import Response


class RoomViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsEmployee]

    queryset = Room.objects.filter()

    serializer_class = RoomSerializer

    serializer_action_classes = {
        "list": RoomReadOnlySerializer,
        "retrieve": RoomReadOnlySerializer,
    }
    filterset_class = RoomFilterSet






