from django.contrib.auth.base_user import BaseUserManager
from safedelete import DELETED_INVISIBLE, DELETED_VISIBLE_BY_PK
from safedelete.managers import SafeDeleteManager

from apps.users.models.role import Role, RolePermissions


class CustomUserManager(SafeDeleteManager, BaseUserManager):
    _safedelete_visibility = DELETED_VISIBLE_BY_PK

    def create_superuser(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Users must have an username")
        user = self.model(username=username)
        user.set_password(password)
        user.is_superuser = True
        user.save(using=self._db)
        try:
            admin = Role.objects.get(name=RolePermissions.ADMIN)
            employee = Role.objects.get(name=RolePermissions.EMPLOYEE)
            customer = Role.objects.get(name=RolePermissions.CUSTOMER)
            guest = Role.objects.get(name=RolePermissions.GUEST)
            user.roles.add(admin)
            user.roles.add(employee)
            user.roles.add(customer)
            user.roles.add(guest)
            user.save(using=self._db)
        except Exception:
            raise ValueError("Error")
        return user
