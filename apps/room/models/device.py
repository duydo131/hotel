import uuid

from django.db import models
from safedelete import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteMixin

from apps.room.models.room_category import RoomCategory
from apps.hotel.models import Hotel


class Device(SafeDeleteMixin):
    _safedelete_policy = SOFT_DELETE_CASCADE

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, null=True, blank=True)
    price = models.BigIntegerField(blank=True, default=0)
    image_url = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "device"
        ordering = ["name"]

    def __str__(self):
        return self.name
