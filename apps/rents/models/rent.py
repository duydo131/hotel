import uuid

from django.db import models
from safedelete import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteMixin


class Rent(SafeDeleteMixin):
    _safedelete_policy = SOFT_DELETE_CASCADE

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    discount = models.BigIntegerField(null=True, blank=True)
    totalAmount = models.BigIntegerField(null=True, blank=True)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rents",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "rent"
        ordering = ["created_at"]

    def __str__(self):
        return str(self.id)
