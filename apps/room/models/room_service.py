import uuid

from django.db import models
from safedelete import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteMixin

from apps.room.models import Room, Service


class RoomService(SafeDeleteMixin):
    _safedelete_policy = SOFT_DELETE_CASCADE

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    room = models.OneToOneField(
        Room,
        on_delete=models.CASCADE,
        related_name="service",
        blank=True
    )

    services = models.ManyToManyField(
        Service,
        related_name="services",
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "room_service"

    def __str__(self):
        return self.id
