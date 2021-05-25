from django.db import transaction
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AnonymousUser
from rest_framework import viewsets

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from apps.rents.models import RentDetail
from apps.room.filters import RoomServiceFilterSet
from apps.room.models import Room, Service
from apps.room.models.room_service import RoomService
from apps.room.serializers.room_service import RoomServiceSerializer, RoomServiceReadOnlySerializer
from core.mixins import GetSerializerClassMixin
from core.permissions import IsCustomer


class RoomServiceViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsCustomer]

    queryset = RoomService.objects.filter()

    serializer_class = RoomServiceSerializer

    serializer_action_classes = {
        "list": RoomServiceReadOnlySerializer,
        "retrieve": RoomServiceReadOnlySerializer,
    }
    filterset_class = RoomServiceFilterSet

    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)

                room_service_id = dict(serializer.data)['id']
                room_service = RoomService.objects.get(id=room_service_id)
                if not room_service or isinstance(request.user, AnonymousUser):
                    raise APIException(
                        _("Cannot add service"),
                        status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )
                id_room = request.data['room']
                services = request.data['services']
                rent_id = request.data['rent']

                room = Room.objects.get(id=id_room)
                rent = RentDetail.objects.get(id=rent_id)
                list_service = [Service.objects.get(id=service_id) for service_id in services]
                room_service.room = room
                room_service.rent = rent
                for service in list_service:
                    room_service.services.add(service)
                room_service.save()
                serializer = RoomServiceReadOnlySerializer(room_service)
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            raise APIException(
                _("Error Server"),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
