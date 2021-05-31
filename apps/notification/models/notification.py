import uuid

from django.db import models
from django.db.models import DO_NOTHING
from safedelete import SOFT_DELETE_CASCADE, HARD_DELETE
from safedelete.models import SafeDeleteMixin

from django.utils.translation import gettext_lazy as _

from apps.hotel.models import Hotel
from apps.rents.models import Rent
from apps.users.models import User


class NotificationType(models.TextChoices):
    RENT = "RENT", _("RENT")
    UNKNOWN = "UNKNOWN", _("UNKNOWN")


class Notification(SafeDeleteMixin):
    _safedelete_policy = HARD_DELETE

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hotel = models.ForeignKey(
        Hotel,
        on_delete=DO_NOTHING,
    )
    rent = models.OneToOneField(
        Rent,
        on_delete=DO_NOTHING,
    )
    staff = models.ForeignKey(
        User,
        on_delete=DO_NOTHING,
        related_name="notifications",
        null=True,
        blank=True
    )
    type = models.CharField(
        choices=NotificationType.choices,
        max_length=20,
        default=NotificationType.UNKNOWN,
    )
    status = models.BooleanField(default=False)
    content = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "notification"
        ordering = ["created_at"]

    def __str__(self):
        return str(self.id)
