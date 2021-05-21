import uuid

from django.db import models
from safedelete import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteMixin

from apps.room.models.room_category import RoomCategory
from apps.hotel.models import Hotel


class Room(SafeDeleteMixin):
    _safedelete_policy = SOFT_DELETE_CASCADE

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name="rooms",
        blank=True,
        null=True
    )
    name = models.CharField(max_length=20, null=True, blank=True)
    category = models.ForeignKey(
        RoomCategory,
        on_delete=models.CASCADE,
        related_name="rooms",
        null=True,
        blank=True
    )
    price = models.BigIntegerField(blank=True)
    price_now = models.BigIntegerField(blank=True, null=True)
    status = models.BooleanField(default=True)
    image_url = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    adult = models.IntegerField(default=1)
    children = models.IntegerField(default=1)

    class Meta:
        db_table = "room"
        ordering = ["name"]

    def __str__(self):
        return self.name
