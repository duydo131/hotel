from django.db import transaction
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets, status
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from apps.room.filters import RoomFilterSet
from apps.room.models import Room
from apps.room.serializers import RoomSerializer, RoomReadOnlySerializer
from apps.room.serializers.room import RoomDetailReadOnlySerializer
from core.mixins import GetSerializerClassMixin
from core.permissions import IsEmployee


class RoomViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsEmployee]

    serializer_class = RoomSerializer
    serializer_detail_class = RoomDetailReadOnlySerializer

    queryset = Room.objects.all()
    queryset_detail = Room.objects.prefetch_related('services')

    serializer_action_classes = {
        "list": RoomReadOnlySerializer,
        "retrieve": RoomDetailReadOnlySerializer,
    }
    filterset_class = RoomFilterSet

    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                room = (Room.objects
                        .filter(id=dict(serializer.data)['id'])
                        .prefetch_related("category__services").first())
                for service in room.category.services.all():
                    room.services.add(service)
                room.save()
                data = RoomSerializer(room)
                headers = self.get_success_headers(data)
                return Response(data.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as ex:
            raise APIException(
                _("Don't create room : " + str(ex)),
                status.HTTP_404_NOT_FOUND,
            )
