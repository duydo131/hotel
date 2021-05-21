import uuid

from django.db import models
from safedelete import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteMixin

from apps.hotel.models import Hotel
from apps.users.models import User


class Question(SafeDeleteMixin):
    _safedelete_policy = SOFT_DELETE_CASCADE

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hotel = models.ManyToManyField(
        Hotel,
        related_name="places",
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        User,
        related_name="questions",
        blank=True,
        null=True,
    )
    content = models.TextField(null=True, blank=True)
    like = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "question"
        ordering = ["created_at"]

    def __str__(self):
        return self.id
