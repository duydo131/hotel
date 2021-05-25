from django.db import transaction
from rest_framework import viewsets

from apps.hotel.models import Hotel
from apps.rents.filters import FeedbackFilterSet
from apps.rents.models import Feedback, Rent
from apps.rents.serializers import FeedbackSerializer, FeedbackReadOnlySerializer
from core.mixins import GetSerializerClassMixin
from core.permissions import IsCustomer
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.response import Response


def updateRating(rating, count, feedback):
    rating.comfortable = (rating.comfortable * count + feedback.comfortable) / (count + 1)
    rating.address = (rating.address * count + feedback.address) / (count + 1)
    rating.wifi_free = (rating.wifi_free * count + feedback.wifi_free) / (count + 1)
    rating.staff = (rating.staff * count + feedback.staff) / (count + 1)
    rating.convenirent = (rating.convenirent * count + feedback.convenirent) / (count + 1)
    rating.clean = (rating.clean * count + feedback.clean) / (count + 1)


class FeedbackViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = [IsCustomer]

    queryset = Feedback.objects.filter()

    serializer_class = FeedbackSerializer

    serializer_action_classes = {
        "list": FeedbackReadOnlySerializer,
        "retrieve": FeedbackReadOnlySerializer,
    }
    filterset_class = FeedbackFilterSet

    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                id_rent = request.data['rent']
                id_hotel = request.data['hotel']
                rent = Rent.objects.filter(id=id_rent).first()
                hotel = Hotel.objects.filter(id=id_hotel).first()
                if not rent:
                    raise APIException(
                        _("Don't find rent detail"),
                        status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )
                if rent.feedback:
                    raise APIException(
                        _("Feedback exist"),
                        status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                id_feedback = dict(serializer.data)['id']
                feedback = Feedback.objects.get(id=id_feedback)
                if not feedback:
                    raise APIException(
                        _("Cannot create feedback"),
                        status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )

                rent.feedback = feedback
                rent.save()
                count = hotel.feedbacks.count()
                rating = hotel.rating
                updateRating(rating, count, feedback)
                rating.save()
                hotel.feedbacks.add(feedback)
                hotel.save()
                serializer = FeedbackReadOnlySerializer(feedback)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            raise APIException(
                _("Error Server"),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )







