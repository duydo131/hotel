from rest_framework import viewsets

from apps.rents.filters import FeedbackFilterSet
from apps.rents.models import Feedback, RentDetail
from apps.rents.serializers import FeedbackSerializer, FeedbackReadOnlySerializer
from core.mixins import GetSerializerClassMixin
from core.permissions import IsCustomer
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.response import Response


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
        id_detail = request.data['rent']
        detail = RentDetail.objects.filter(id=id_detail).first()
        print(detail)
        if not detail:
            raise APIException(
                _("Don't find rent detail"),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        if detail.feedback:
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

        detail.feedback = feedback
        detail.save()
        serializer = FeedbackReadOnlySerializer(feedback)
        return Response(serializer.data, status=status.HTTP_201_CREATED)






