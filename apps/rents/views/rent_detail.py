from rest_framework import viewsets

from apps.rents.filters import RentDetailFilterSet
from apps.rents.models import RentDetail
from apps.rents.serializers import RentDetailSerializer, RentDetailReadOnlySerializer
from core.mixins import GetSerializerClassMixin
from core.permissions import IsCustomer


class RentDetailViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsCustomer]

    queryset = RentDetail.objects.all()
    queryset_detail = RentDetail.objects.all()

    serializer_class = RentDetailSerializer
    serializer_detail_class = RentDetailReadOnlySerializer

    serializer_action_classes = {
        "list": RentDetailReadOnlySerializer,
        "retrieve": RentDetailReadOnlySerializer,
    }
    filterset_class = RentDetailFilterSet
