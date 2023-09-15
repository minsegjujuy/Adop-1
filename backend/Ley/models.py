from django.db import models
from Procedimiento.models import TipoProcedimiento
from BaseModel.models import BaseModel
from auditlog.registry import auditlog


class Ley(BaseModel):
    fk_tipo_procedimiento = models.ForeignKey(
        TipoProcedimiento, on_delete=models.CASCADE
    )
    ley = models.TextField(unique=True)


class Articulo(BaseModel):
    fk_ley = models.ForeignKey("Ley", on_delete=models.CASCADE)
    articulo = models.TextField(unique=True)


class Inciso(BaseModel):
    fk_articulo = models.ForeignKey("Articulo", on_delete=models.CASCADE)
    inciso = models.TextField(unique=True)


auditlog.register(
    Ley,
    exclude_fields=[
        "updated_at",
        "created_at",
        "deleted_at",
    ],
)
auditlog.register(
    Articulo,
    exclude_fields=[
        "updated_at",
        "created_at",
        "deleted_at",
    ],
)
auditlog.register(
    Inciso,
    exclude_fields=[
        "updated_at",
        "created_at",
        "deleted_at",
    ],
)
