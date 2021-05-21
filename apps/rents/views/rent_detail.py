from rest_framework import viewsets

from apps.rents.filters import RentDetailFilterSet
from apps.rents.models import Rent, RentDetail
from apps.rents.serializers import RentDetailSerializer, RentDetailReadOnlySerializer
from apps.room.models import Room
from core.mixins import GetSerializerClassMixin
from core.permissions import IsCustomer
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.response import Response


class RentDetailViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsCustomer]

    queryset = RentDetail.objects.filter()

    serializer_class = RentDetailSerializer

    serializer_action_classes = {
        "list": RentDetailReadOnlySerializer,
        "retrieve": RentDetailReadOnlySerializer,
    }
    filterset_class = RentDetailFilterSet

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        id_detail = dict(serializer.data)['id']
        detail = RentDetail.objects.get(id=id_detail)
        if not detail:
            raise APIException(
                _("Cannot create room"),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        id_rent = request.data['rent']
        id_room = request.data['room']
        rent = Rent.objects.get(id=id_rent)
        room = Room.objects.get(id=id_room)
        if not rent and not room:
            raise APIException(
                _("Error Server"),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        detail.rent = rent
        detail.room = room
        serializer = RentDetailReadOnlySerializer(detail)
        return Response(serializer.data, status=status.HTTP_201_CREATED)






