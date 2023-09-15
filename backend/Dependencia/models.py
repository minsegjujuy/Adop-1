from django.db import models
from BaseModel.models import BaseModel
from auditlog.registry import auditlog


class Inspectora(BaseModel):
    nombre_inspectora = models.CharField(
        max_length=255, null=True, blank=True, unique=True
    )


class UnidadRegional(BaseModel):
    unidad_regional = models.CharField(max_length=23, default="", unique=True)


class Dependencia(BaseModel):
    fk_unidad_regional = models.ForeignKey("UnidadRegional", on_delete=models.CASCADE)
    fk_inspectora = models.ForeignKey("Inspectora", on_delete=models.CASCADE, null=True)
    jurisdiccion = models.CharField(null=False, max_length=100)
    # activar luego de la primera migracion
    # operativos = models.ManyToManyField('DependenciaOperativos', db_table='dependencia_operativos', related_name='operativos') #comentar para la primera migracion


class DependenciaOperativos(BaseModel):
    fk_dependencia = models.ForeignKey("Dependencia.Dependencia", on_delete=models.CASCADE)
    fk_operativo = models.ForeignKey("Operativos.Operativo", on_delete=models.CASCADE)


auditlog.register(
    Inspectora,
    exclude_fields=[
        "updated_at",
        "created_at",
        "deleted_at",
    ],
)
auditlog.register(
    UnidadRegional,
    exclude_fields=[
        "updated_at",
        "created_at",
        "deleted_at",
    ],
)
auditlog.register(
    Dependencia,
    exclude_fields=[
        "updated_at",
        "created_at",
        "deleted_at",
    ],
)
auditlog.register(
    DependenciaOperativos,
    exclude_fields=[
        "updated_at",
        "created_at",
        "deleted_at",
    ],
)
