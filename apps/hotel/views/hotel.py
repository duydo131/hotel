from django.contrib.auth.models import AnonymousUser
from rest_framework import viewsets

from apps.hotel.filters import HotelFilterSet
from core.mixins import GetSerializerClassMixin
from apps.hotel.models import Hotel, Rating
from apps.hotel.serializers import HotelSerializer, HotelReadOnlySerializer

from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException
from core.permissions import IsEmployee
from rest_framework import status
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action


class HotelViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsEmployee]

    queryset = Hotel.objects.all()

    serializer_class = HotelSerializer

    serializer_action_classes = {
        "list": HotelReadOnlySerializer,
        "retrieve": HotelReadOnlySerializer,
    }
    filterset_class = HotelFilterSet

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        hotel_id = dict(serializer.data)['id']
        hotel = Hotel.objects.get(id=hotel_id)
        if not hotel or isinstance(request.user, AnonymousUser):
            raise APIException(
                _("Cannot find user"),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        hotel.staff.add(request.user)
        hotel.save()
        rating = Rating()
        rating.hotel = hotel
        rating.save()
        serializer = HotelReadOnlySerializer(hotel)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)