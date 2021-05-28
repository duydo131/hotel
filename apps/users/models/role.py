import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from safedelete import SOFT_DELETE_CASCADE, HARD_DELETE
from safedelete.models import SafeDeleteMixin


class RolePermissions(models.TextChoices):
    CUSTOMER = "CUSTOMER", _("CUSTOMER")
    ADMIN = "ADMIN", _("ADMIN")
    EMPLOYEE = "EMPLOYEE", _("EMPLOYEE")
    GUEST = "GUEST", _("GUEST")


class Role(SafeDeleteMixin):
    _safedelete_policy = HARD_DELETE

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        choices=RolePermissions.choices,
        max_length=20,
        default=RolePermissions.GUEST,
    )
    description = models.CharField(max_length=20, null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "role"
        ordering = ["created_at"]

    def __str__(self):
        return self.name
