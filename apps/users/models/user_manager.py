from django.contrib.auth.base_user import BaseUserManager
from safedelete.managers import SafeDeleteManager

from apps.users.models.role import Role, RolePermissions


class CustomUserManager(SafeDeleteManager, BaseUserManager):
    def create_superuser(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Users must have an username")

        admin = Role.objects.get(name=RolePermissions.ADMIN)
        if not admin:
            raise ValueError("Admin not define")

        user = self.model(username=username)
        user.set_password(password)
        user.role = admin
        user.save(using=self._db)
        return user
