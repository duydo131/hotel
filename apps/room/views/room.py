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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        id_room = dict(serializer.data)['id']
        room = Room.objects.get(id=id_room)
        if not room:
            raise APIException(
                _("Cannot create room"),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        id_hotel = request.data['hotel']
        id_cat = request.data['category']
        hotel = Hotel.objects.get(id=id_hotel)
        category = RoomCategory.objects.get(id=id_cat)
        if not hotel and not category:
            raise APIException(
                _("Error Server"),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        room.hotel = hotel
        room.category = category
        room.save()
        serializer = RoomReadOnlySerializer(room)
        return Response(serializer.data, status=status.HTTP_201_CREATED)






