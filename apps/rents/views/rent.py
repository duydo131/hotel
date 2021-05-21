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
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        id_rent = dict(serializer.data)['id']
        rent = Rent.objects.get(id=id_rent)
        if not rent:
            raise APIException(
                _("Cannot create rent"),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        customer = request.user
        if not customer:
            raise APIException(
                _("Error Server"),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        rent.user = customer
        rent.save()
        serializer = RentReadOnlySerializer(rent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)






