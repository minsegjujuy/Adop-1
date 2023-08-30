from django.db import models
from Operativos.models import Operativo
from BaseModel.models import BaseModel


class TipoServicio(BaseModel):
    tipo_servicio = models.TextField()


class TipoRecurso(BaseModel):
    tipo_recurso = models.TextField()


class Servicio(BaseModel):
    fk_operativo = models.ForeignKey(Operativo, on_delete=models.CASCADE)
    fk_tipo_servicio = models.ForeignKey(
        "TipoServicio", on_delete=models.CASCADE, null=True
    )
    fk_tipo_recurso = models.ForeignKey(
        "TipoRecurso", on_delete=models.CASCADE, null=True
    )
    cant_recursos = models.IntegerField()
