import uuid

from django.db import models
from safedelete import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteMixin

from apps.hotel.models import Hotel


class AroundPlace(SafeDeleteMixin):
    _safedelete_policy = SOFT_DELETE_CASCADE

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=True, blank=True)
    hotel = models.ManyToManyField(
        Hotel,
        related_name="places",
        blank=True,
        null=True,
    )
    address = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    range = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "around_place"
        ordering = ["range"]

    def __str__(self):
        return self.name + (": " + self.category) if self.category else ""
