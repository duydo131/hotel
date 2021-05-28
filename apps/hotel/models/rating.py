import uuid

from django.db import models
from safedelete import SOFT_DELETE_CASCADE, HARD_DELETE
from safedelete.models import SafeDeleteMixin

from apps.hotel.models import Hotel


class Rating(SafeDeleteMixin):
    _safedelete_policy = HARD_DELETE

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comfortable = models.FloatField(default=0)
    address = models.FloatField(default=0)
    wifi_free = models.FloatField(default=0)
    staff = models.FloatField(default=0)
    convenirent = models.FloatField(default=0)
    clean = models.FloatField(default=0)
    hotel = models.OneToOneField(
        Hotel,
        on_delete=models.CASCADE,
        related_name="rating"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "rating"

    def __str__(self):
        return str(self.id)
