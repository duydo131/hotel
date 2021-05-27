import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from safedelete import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteMixin


class Hotel(SafeDeleteMixin):
    _safedelete_policy = SOFT_DELETE_CASCADE

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    fax = models.CharField(max_length=11, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    nation = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    stars = models.IntegerField(null=True, blank=True)

    image_url = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = "hotel"
        ordering = ["name"]

    def __str__(self):
        return self.name
