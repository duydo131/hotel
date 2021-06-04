from datetime import datetime

from django.contrib.auth.models import AnonymousUser
from django.db import transaction
from django.db.models import Count, Func, Sum, Q
from rest_framework import viewsets
from rest_framework.decorators import action

from apps.hotel.filters import HotelFilterSet
from apps.hotel.serializers.hotel import StatisticalHotelReadOnlySerializer
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

    queryset = Hotel.objects.annotate(total_room=Count('rooms', distinct=True))

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

    @action(
        methods=["GET"],
        detail=False,
        url_path="statistical",
        url_name="statistical",
        permission_classes=[IsEmployee],
        filterset_class=None,
        pagination_class=None,
    )
    def statistical(self, request, *args, **kwargs):
        month = datetime.now().month - 1
        queryset = self.queryset.filter(
            Q(rents__start_date__month=month)
            & Q(rents__status=True)
            & Q(rents__done=True)
        )
        # queryset = Hotel.objects.all()
        if 'id' in request.GET:
            hotel = request.GET['id']
            queryset = queryset.filter(pk=hotel).distinct()

        statistical = queryset.annotate(
            turnove=Sum('rents__totalAmount') / Count('rooms', distinct=True),
            total_rent=Count('rents', distinct=True),
        )
        serializer = StatisticalHotelReadOnlySerializer(statistical, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

