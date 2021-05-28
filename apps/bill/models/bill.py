import uuid

from django.db import models
from safedelete import SOFT_DELETE_CASCADE, HARD_DELETE
from safedelete.models import SafeDeleteMixin

from apps.hotel.models import Hotel
from apps.rents.models import Rent


class Bill(SafeDeleteMixin):
    _safedelete_policy = HARD_DELETE

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name="bills",
        blank=True,
    )
    totalAmount = models.BigIntegerField(null=True, blank=True)
    customer = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="bills",
        blank=True,
    )
    rent = models.OneToOneField(
        Rent,
        on_delete=models.CASCADE,
        related_name="bill",
        blank=True,
    )
    staff = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="all_bill",
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "bill"
        ordering = ["created_at"]

    def __str__(self):
        return self.id
