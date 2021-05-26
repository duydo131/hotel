from rest_framework import viewsets

from apps.rents.filters import RentFilterSet
from apps.rents.models import Rent
from apps.rents.serializers.rent import RentSerializer, RentReadOnlySerializer
from core.mixins import GetSerializerClassMixin
from core.permissions import IsCustomer
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.response import Response


class RentViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsCustomer]

    queryset = Rent.objects.filter()

    serializer_class = RentSerializer

    serializer_action_classes = {
        "list": RentReadOnlySerializer,
        "retrieve": RentReadOnlySerializer,
    }
    filterset_class = RentFilterSet

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        return super().create(request, *args, **kwargs)






