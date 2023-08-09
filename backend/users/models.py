from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UsuarioManager
from Dependencia.models import Dependencia, UnidadRegional


class Rol(models.Model):
    rol = models.CharField(max_length=13, unique=True)


class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField("Nombre de Usuario", max_length=100, unique=True)
    email = models.EmailField("Correo Electronico", max_length=254, unique=True)
    nombres = models.CharField("Nombres", max_length=200, blank=True, null=True)
    apellidos = models.CharField("Apellidos", max_length=200, blank=True, null=True)
    rol = models.ForeignKey("Rol", null=False, on_delete=models.CASCADE)
    jurisdiccion = models.ForeignKey(
        Dependencia,
        name="jurisdiccion",
        null=True,
        default=None,
        on_delete=models.CASCADE,
    )
    unidad_regional = models.ForeignKey(
        UnidadRegional,
        name="unidad_regional",
        null=True,
        default=None,
        on_delete=models.CASCADE,
    )
    usuario_activo = models.BooleanField(default=True)

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser
