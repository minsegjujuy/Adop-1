from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):

    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Empleado(models.Model):
    User = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="empleados"
    )
    nivel_permiso = models.CharField(
        "nivel permiso", max_length=50, default="operador")

    class Meta:
        verbose_name_plural = "Empleados"
        permissions = (
            # Super Admin
            ("administrador", "Administrador"),
            # operarios empleados:
            ("operador", "Operador"),
            # general
            ("general", "General"),
        )
