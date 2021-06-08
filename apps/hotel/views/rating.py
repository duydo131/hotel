from rest_framework import viewsets

from apps.hotel.filters import HotelFilterSet, RatingFilterSet
from core.mixins import GetSerializerClassMixin
from apps.hotel.models import Hotel, Rating
from apps.hotel.serializers import HotelSerializer, HotelReadOnlySerializer, RatingSerializer, RatingReadOnlySerializer

from core.permissions import IsAdmin


class RatingViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsAdmin]

    queryset = Rating.objects.all()
    queryset_detail = Rating.objects.all()
    serializer_class = RatingSerializer

    serializer_action_classes = {
        "list": RatingReadOnlySerializer,
        "retrieve": RatingReadOnlySerializer,
    }
    filterset_class = RatingFilterSet
