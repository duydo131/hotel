from builtins import Exception

from django.db import transaction
from rest_framework import viewsets, status
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException

from apps.hotel.models import Hotel
from apps.notification.models import NotificationType
from apps.rents.filters import RentFilterSet
from apps.rents.models import Rent
from apps.rents.serializers import RentDetailSerializer
from apps.rents.serializers.rent import RentSerializer, RentReadOnlySerializer, RentGetDetailReadOnlySerializer
from core.mixins import GetSerializerClassMixin
from core.permissions import IsCustomer
from core.task import update_cache
from core.utils import create_model, get_values_token, GenCachePrefixKey
from apps.rents.task import notification


class RentViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsCustomer]

    queryset = Rent.objects.all()
    queryset_detail = Rent.objects.prefetch_related('details')

    serializer_class = RentSerializer
    serializer_detail_class = RentGetDetailReadOnlySerializer

    serializer_action_classes = {
        "list": RentReadOnlySerializer,
        "retrieve": RentGetDetailReadOnlySerializer,
    }
    filterset_class = RentFilterSet

    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                details = request.data['details']
                rooms = [detail['room'] for detail in details]
                hotel = Hotel.objects.filter(rooms__id__in=rooms).distinct().first()

                request.data['user'] = request.user.id
                request.data['hotel'] = hotel.id
                x = super().create(request, *args, **kwargs)
                rent_id = x.data['id']
                for detail in details:
                    detail['rent'] = rent_id
                    create_model(detail, RentDetailSerializer)

                notification.apply_async(args=[rent_id, NotificationType.RENT, hotel.id])
                return x
        except Exception as ex:
            raise APIException(
                _("Cannot create rent : " + str(ex)),
                status.HTTP_400_BAD_REQUEST,
            )
