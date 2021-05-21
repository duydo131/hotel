import uuid

from django.db import models
from safedelete import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteMixin


class Feedback(SafeDeleteMixin):
    _safedelete_policy = SOFT_DELETE_CASCADE

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comfortable = models.IntegerField()
    address = models.IntegerField()
    wifi_free = models.IntegerField()
    staff = models.IntegerField()
    convenirent = models.IntegerField()
    clean = models.IntegerField()
    content = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "feedback"
        ordering = ["created_at"]

    def __str__(self):
        return str(self.id)
