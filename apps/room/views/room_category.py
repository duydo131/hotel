from rest_framework import viewsets

from apps.room.filters import RoomCategoryFilterSet
from apps.room.models import RoomCategory
from apps.room.serializers import RoomSerializer
from apps.room.serializers.room_category import RoomCategorySerializer
from core.mixins import GetSerializerClassMixin
from core.permissions import IsCustomer


class RoomCategoryViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsCustomer]

    queryset = RoomCategory.objects.filter()

    serializer_class = RoomCategorySerializer

    # serializer_action_classes = {
    #     "list": RoomReadOnlySerializer,
    #     "retrieve": RoomReadOnlySerializer,
    # }
    filterset_class = RoomCategoryFilterSet





