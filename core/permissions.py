from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions
from rest_framework.permissions import BasePermission
from apps.users.models.role import RolePermissions


# from apps.external_apps.models.app import App
#
#
# class AppPermission(BasePermission):
#     """
#     Allows access only to authenticated users.
#     """
#
#     def has_permission(self, request, view):
#         if isinstance(request.user, App):
#             return request.user.active
#         return False


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if isinstance(request.user, AnonymousUser):
            return False
        return RolePermissions.ADMIN in [role.name for role in request.user.roles.all()] \
               and request.user.is_authenticated


class IsEmployee(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if isinstance(request.user, AnonymousUser):
            return False
        return RolePermissions.EMPLOYEE in [role.name for role in request.user.roles.all()] \
               and request.user.is_authenticated


class IsCustomer(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if isinstance(request.user, AnonymousUser):
            return False
        return RolePermissions.CUSTOMER in [role.name for role in request.user.roles.all()] \
               and request.user.is_authenticated
