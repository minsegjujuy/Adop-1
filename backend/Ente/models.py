from django.db import models

from BaseModel.models import BaseModel


class Ente(BaseModel):
    nombre = models.CharField(max_length=150)
    # direccion = models.CharField(max_length=255)
