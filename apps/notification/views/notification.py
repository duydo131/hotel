from rest_framework import viewsets

from apps.notification.filters import NotificationFilterSet
from apps.notification.models import Notification
from apps.notification.serializers import NotificationSerializer, NotificationReadOnlySerializer
from apps.notification.serializers.notification import NotificationDetailReadOnlySerializer
from core.mixins import GetSerializerClassMixin
from core.permissions import IsEmployee


class NotificationViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsEmployee]

    queryset = Notification.objects.all()
    queryset_detail = Notification.objects.select_related('rent')
    serializer_class = NotificationSerializer
    serializer_detail_class = NotificationDetailReadOnlySerializer

    serializer_action_classes = {
        "list": NotificationReadOnlySerializer,
        "retrieve": NotificationDetailReadOnlySerializer,
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
