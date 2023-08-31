from django.db import models
from Procedimiento.models import Procedimiento
from BaseModel.models import BaseModel
from auditlog.registry import auditlog


class TipoSecuestro(BaseModel):
    tipo_secuestro = models.CharField(max_length=20)


class Secuestro(BaseModel):
    fk_tipo_secuestro = models.ForeignKey("TipoSecuestro", on_delete=models.CASCADE)
    fk_procedimiento = models.ForeignKey(Procedimiento, on_delete=models.CASCADE)
    descripcion = models.TextField()

auditlog.register(TipoSecuestro, exclude_fields=['updated_at','created_at', 'deleted_at'])
auditlog.register(Secuestro, exclude_fields=['updated_at','created_at', 'deleted_at'])