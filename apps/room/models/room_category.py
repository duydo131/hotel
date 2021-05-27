import uuid

from django.db import models
from safedelete import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteMixin
from apps.room.models.service import Service


class RoomCategory(SafeDeleteMixin):
    _safedelete_policy = SOFT_DELETE_CASCADE

    name = models.CharField(max_length=100, null=True, blank=True, unique=True)
    description = models.TextField(null=True, blank=True)
    services = models.ManyToManyField(
        Service,
        related_name="room_categorys",
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "room_category"
        ordering = ["name"]

    def __str__(self):
        return self.name
