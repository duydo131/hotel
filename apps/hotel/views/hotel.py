from datetime import datetime

from django.contrib.auth.models import AnonymousUser
from django.db import transaction
from django.db.models import Count, Sum, Q
from django.utils.decorators import decorator_from_middleware_with_args
# from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.decorators import action

from apps.hotel.filters import HotelFilterSet
from apps.hotel.serializers.hotel import StatisticalHotelReadOnlySerializer, HotelDetailReadOnlySerializer
from core.mixins import GetSerializerClassMixin
from apps.hotel.models import Hotel, Rating
from apps.hotel.serializers import HotelSerializer, HotelReadOnlySerializer

from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException
from core.permissions import IsEmployee, IsManager
from rest_framework import status
from rest_framework.response import Response


class HotelViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsEmployee]

    queryset = Hotel.objects.annotate(total_room=Count('rooms', distinct=True))
    queryset_detail = Hotel.objects.prefetch_related('rooms').annotate(total_room=Count('rooms', distinct=True))

    serializer_class = HotelSerializer
    serializer_detail_class = HotelDetailReadOnlySerializer

    serializer_action_classes = {
        "list": HotelReadOnlySerializer,
        "retrieve": HotelDetailReadOnlySerializer,
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
        except Exception as ex:
            raise APIException(
                _("Error Server : " + str(ex)),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


    @action(
        methods=["GET"],
        detail=False,
        url_path="statistic",
        url_name="statistic",
        permission_classes=[IsEmployee, IsManager],
        filterset_class=None,
        pagination_class=None,

    )
    # @cache_page(200)
    def statistic(self, request, *args, **kwargs):
        print("cache now")
        month = datetime.now().month
        queryset = Hotel.objects.filter(pk=request.user.hotel_id).filter(
            Q(rents__start_date__month=month)
            & Q(rents__status=True)
            & Q(rents__done=True)
        ).distinct()

        statistics = queryset.annotate(
            turnove=Sum('rents__total_amount'),
            total_rent=Count('rents', distinct=True),
        ).first()

        serializer = StatisticalHotelReadOnlySerializer(statistics)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
