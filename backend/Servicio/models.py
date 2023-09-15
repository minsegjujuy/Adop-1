from django.db import models
from Operativos.models import Operativo
from BaseModel.models import BaseModel
from auditlog.registry import auditlog


class TipoServicio(BaseModel):
    tipo_servicio = models.TextField(unique=True)


class TipoRecurso(BaseModel):
    tipo_recurso = models.TextField(unique=True)


class Servicio(BaseModel):
    fk_operativo = models.ForeignKey(Operativo, on_delete=models.CASCADE)
    fk_tipo_servicio = models.ForeignKey(
        "TipoServicio", on_delete=models.CASCADE, null=True
    )
    fk_tipo_recurso = models.ForeignKey(
        "TipoRecurso", on_delete=models.CASCADE, null=True
    )
    cant_recursos = models.IntegerField()


auditlog.register(
    TipoRecurso,
    exclude_fields=[
        "updated_at",
        "created_at",
        "deleted_at",
    ],
)
auditlog.register(
    TipoServicio,
    exclude_fields=[
        "updated_at",
        "created_at",
        "deleted_at",
    ],
)
auditlog.register(
    Servicio,
    exclude_fields=[
        "updated_at",
        "created_at",
        "deleted_at",
    ],
)
