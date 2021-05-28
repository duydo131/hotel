import uuid

from django.db import models
from safedelete import SOFT_DELETE_CASCADE, HARD_DELETE
from safedelete.models import SafeDeleteMixin


class Device(SafeDeleteMixin):
    _safedelete_policy = HARD_DELETE

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, null=True, blank=True)
    price = models.BigIntegerField(blank=True, default=0)
    image_url = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "device"
        ordering = ["name"]

    def __str__(self):
        return self.name
