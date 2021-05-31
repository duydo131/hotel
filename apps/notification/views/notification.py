from django.db import transaction
from rest_framework import viewsets

from apps.hotel.models import Hotel
from apps.notification.filters import NotificationFilterSet
from apps.notification.models import Notification
from apps.notification.serializers import NotificationSerializer, NotificationReadOnlySerializer
from apps.rents.filters import FeedbackFilterSet
from apps.rents.models import Feedback, Rent
from apps.rents.serializers import FeedbackSerializer, FeedbackReadOnlySerializer
from core.mixins import GetSerializerClassMixin
from core.permissions import IsCustomer, IsEmployee
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.response import Response


class NotificationViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsEmployee]

    queryset = Notification.objects.all()

    serializer_class = NotificationSerializer

    serializer_action_classes = {
        "list": NotificationReadOnlySerializer,
        "retrieve": NotificationReadOnlySerializer,
    }
    filterset_class = NotificationFilterSet

    def get_queryset(self):
        queryset = self.queryset.filter(hotel__staff__id__contains=self.request.user.id)
        return queryset

    def update(self, request, *args, **kwargs):
        request.data['staff'] = request.user.id
        response = super().update(request, *args, **kwargs)
        print("Xác nhận đặt phòng")
        return response