from rest_framework import permissions
from django.contrib.auth.models import Group, Permission


class PermisoAdministrador(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_permission(self, request, view):

        return request.user.has_perm("user.administrador")


class PermisoOperador(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.has
    """

    def has_permission(self, request, view):
        return request.user.has_perm("user.operador")


class PermisoFarmaceutico(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_permission(self, request, view):
        return request.user.has_perm("user.general")
