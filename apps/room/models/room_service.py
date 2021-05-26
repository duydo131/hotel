import uuid

from django.db import models
from safedelete import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteMixin

from apps.rents.models import RentDetail
from apps.room.models import Room, Service


class RoomService(SafeDeleteMixin):
    _safedelete_policy = SOFT_DELETE_CASCADE

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="services",
    )

    services = models.ManyToManyField(
        Service,
        related_name="rooms",
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "room_service"
        ordering = ["id"]

    def __str__(self):
        return str(self.id)
