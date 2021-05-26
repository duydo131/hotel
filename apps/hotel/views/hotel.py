from django.contrib.auth.models import AnonymousUser
from django.db import transaction
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
        try:
            with transaction.atomic():
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                hotel = Hotel.objects.get(id=dict(serializer.data)['id'])
                if not hotel and isinstance(request.user, AnonymousUser):
                    raise APIException(
                        _("Cannot find user"),
                        status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )
                hotel.staff.add(request.user)
                rating = Rating()
                rating.hotel = hotel
                rating.save()
                serializer = HotelReadOnlySerializer(hotel)
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            raise APIException(
                _("Error Server"),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )