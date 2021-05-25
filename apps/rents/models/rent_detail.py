import uuid

from django.db import models
from safedelete import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteMixin

from apps.rents.models.rent import Rent
from apps.room.models import Room


class RentDetail(SafeDeleteMixin):
    _safedelete_policy = SOFT_DELETE_CASCADE

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rent = models.ForeignKey(
        Rent,
        on_delete=models.CASCADE,
        related_name="details",
        blank=True,
        null=True,
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="details",
        blank=True,
        null=True,
    )
    price = models.BigIntegerField(blank=True, null=True)
    voucher = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "rent_detail"
        ordering = ["created_at"]

    def __str__(self):
        return str(self.id)
