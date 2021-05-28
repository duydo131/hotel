import uuid

from django.db import models
from safedelete import SOFT_DELETE_CASCADE, HARD_DELETE
from safedelete.models import SafeDeleteMixin

from apps.room.models import Room, Device


class RoomDevice(SafeDeleteMixin):
    _safedelete_policy = HARD_DELETE

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="room_device",
    )
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name="room_device",
    )
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = "room_device"

    def __str__(self):
        return str(self.id)
