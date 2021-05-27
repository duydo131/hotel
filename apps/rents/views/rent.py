from rest_framework import viewsets

from apps.rents.filters import RentFilterSet
from apps.rents.models import Rent
from apps.rents.serializers.rent import RentSerializer, RentReadOnlySerializer
from core.mixins import GetSerializerClassMixin


class RentViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = []

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






