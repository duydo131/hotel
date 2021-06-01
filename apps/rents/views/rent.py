from django.db import transaction
from rest_framework import viewsets, status
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException

from apps.hotel.models import Hotel
from apps.notification.models import Notification, NotificationType
from apps.notification.serializers import NotificationSerializer
from apps.rents.filters import RentFilterSet
from apps.rents.models import Rent
from apps.rents.serializers import RentDetailSerializer
from apps.rents.serializers.rent import RentSerializer, RentReadOnlySerializer
from core.mixins import GetSerializerClassMixin
from core.permissions import IsCustomer
from core.utils import create_model
from templates.notification import notification


class RentViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsCustomer]

    queryset = Rent.objects.filter()

    serializer_class = RentSerializer

    serializer_action_classes = {
        "list": RentReadOnlySerializer,
        "retrieve": RentReadOnlySerializer,
    }
    filterset_class = RentFilterSet

    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                request.data['user'] = request.user.id
                x = super().create(request, *args, **kwargs)
                rent_id = x.data['id']
                details = request.data['details']
                rooms = []
                for detail in details:
                    detail['rent'] = rent_id
                    rooms.append(detail['room'])
                    create_model(detail, RentDetailSerializer)

                hotel = Hotel.objects.filter(rooms__id__in=rooms).distinct().first()

                # notification cho nhaan vieen
                notification.delay(rent_id, NotificationType.RENT, hotel.id)
                return x
        except:
            raise APIException(
                _("Cannot create rent detail!!"),
                status.HTTP_404_NOT_FOUND,
            )

    def list(self, request, *args, **kwargs):
        x = notification.apply_async(queue='low_priority', args=(0, 0, 0))
        print(x)
        return super().list(request, *args, **kwargs)
