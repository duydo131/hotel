from rest_framework import viewsets

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from apps.room.filters import ServiceFilterSet
from django.utils.translation import gettext_lazy as _
from apps.room.models import Service, RoomCategory
from apps.room.serializers.service import ServiceSerializer, ServiceReadOnlySerializer
from core.mixins import GetSerializerClassMixin
from core.permissions import IsEmployee


class ServiceViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsEmployee]

    queryset = Service.objects.filter()

    serializer_class = ServiceSerializer

    serializer_action_classes = {
        "list": ServiceReadOnlySerializer,
        "retrieve": ServiceReadOnlySerializer,
    }
    filterset_class = ServiceFilterSet

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        id_service = dict(serializer.data)['id']
        service = Service.objects.get(id=id_service)
        if not service:
            raise APIException(
                _("Cannot create service"),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        try:
            category = [RoomCategory.objects.get(id=id_cat) for id_cat in request.data['category']]
            for cat in category:
                cat.services.add(service)
                cat.save()
        except Exception as e:
            print(e)
            raise APIException(
                _("Error Server"),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        serializer = ServiceReadOnlySerializer(service)
        return Response(serializer.data, status=status.HTTP_201_CREATED)





