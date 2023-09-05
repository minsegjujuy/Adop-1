from django.db import models
from Dependencia.models import Dependencia, UnidadRegional
from Persona.models import Persona
from BaseModel.models import BaseModel
from auditlog.registry import auditlog


class Jerarquia(BaseModel):
    nombre = models.CharField(max_length=100, unique=True)
    nombre_largo = models.CharField(max_length=255, unique=True)


class Personal(BaseModel):
    legajo = models.IntegerField(primary_key=True)
    fk_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, default=None)
    # fk_tipo_funcion = models.ForeignKey('TipoFuncion', on_delete=models.CASCADE)
    fk_jerarquia = models.ForeignKey("Jerarquia", on_delete=models.CASCADE)
    fk_destino = models.ForeignKey(Dependencia, on_delete=models.CASCADE, null=True)
    fk_jurisdiccion = models.ForeignKey(
        UnidadRegional, on_delete=models.CASCADE, null=True
    )


class Categoria(BaseModel):
    nombre = models.CharField(max_length=100)


class SubCategoria(BaseModel):
    nombre = models.CharField(max_length=100)
    fk_categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)


class Funcionario(BaseModel):
    fk_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fk_categoria = models.ForeignKey("SubCategoria", on_delete=models.CASCADE)
    fecha_inicio = models.DateField(null=False)
    fecha_fin = models.DateField(null=True)


auditlog.register(Jerarquia, exclude_fields=["updated_at", "created_at", "deleted_at"])
auditlog.register(Personal, exclude_fields=["updated_at", "created_at", "deleted_at"])
auditlog.register(Categoria, exclude_fields=["updated_at", "created_at", "deleted_at"])
auditlog.register(SubCategoria, exclude_fields=["updated_at", "created_at", "deleted_at"])
auditlog.register(Funcionario, exclude_fields=["updated_at", "created_at", "deleted_at"])
