import uuid

from django.db import models
from django.db.models import DO_NOTHING
from safedelete import SOFT_DELETE_CASCADE, HARD_DELETE
from safedelete.models import SafeDeleteMixin

from apps.hotel.models import Hotel
from apps.rents.models.feedback import Feedback


class Rent(SafeDeleteMixin):
    _safedelete_policy = HARD_DELETE

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    discount = models.BigIntegerField(null=True, blank=True)
    totalAmount = models.BigIntegerField(null=True, blank=True)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rents",
    )
    feedback = models.OneToOneField(
        Feedback,
        on_delete=models.DO_NOTHING,
        related_name="rent",
        blank=True,
        null=True,
    )
    hotel = models.ForeignKey(
        Hotel,
        on_delete=DO_NOTHING,
        related_name='rents',
    )
    status = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "rent"
        ordering = ["created_at"]

    def __str__(self):
        return str(self.id)
