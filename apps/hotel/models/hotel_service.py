import uuid

from django.db import models
from safedelete import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteMixin

from apps.hotel.models import Hotel


class HotelService(SafeDeleteMixin):
    _safedelete_policy = SOFT_DELETE_CASCADE

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=True, blank=True)
    hotel = models.ManyToManyField(
        Hotel,
        related_name="services",
        null=True,
        blank=True,
    )
    status = models.BooleanField(default=True)
    voucher = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.BigIntegerField(default=0)

    class Meta:
        db_table = "hotel_service"

    def __str__(self):
        return self.id
