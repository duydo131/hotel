from rest_framework import viewsets

from apps.room.filters import RoomCategoryFilterSet
from apps.room.models import RoomCategory
from apps.room.serializers import RoomSerializer
from apps.room.serializers.room_category import RoomCategorySerializer, RoomCategoryReadOnlySerializer, \
    RoomCategoryDetailReadOnlySerializer
from core.mixins import GetSerializerClassMixin
from core.permissions import IsCustomer, IsEmployee


class RoomCategoryViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsEmployee]

    queryset = RoomCategory.objects.filter()
    queryset_detail = RoomCategory.objects.prefetch_related('services')

    serializer_class = RoomCategorySerializer
    serializer_detail_class = RoomCategoryDetailReadOnlySerializer

    serializer_action_classes = {
        "list": RoomCategoryReadOnlySerializer,
        "retrieve": RoomCategoryDetailReadOnlySerializer,
    }
    filterset_class = RoomCategoryFilterSet





