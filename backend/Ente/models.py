from django.db import models
from BaseModel.models import BaseModel
from auditlog.registry import auditlog


class Ente(BaseModel):
    nombre = models.CharField(max_length=150, unique=True)
    # direccion = models.CharField(max_length=255)


auditlog.register(Ente, exclude_fields=["updated_at", "created_at", "deleted_at"])
