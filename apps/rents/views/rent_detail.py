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
