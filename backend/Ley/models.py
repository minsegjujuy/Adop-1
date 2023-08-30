from django.db import models
from Procedimiento.models import TipoProcedimiento
from BaseModel.models import BaseModel


class Ley(BaseModel):
    fk_tipo_procedimiento = models.ForeignKey(TipoProcedimiento, on_delete=models.CASCADE)
    ley = models.TextField()


class Articulo(BaseModel):
    fk_ley = models.ForeignKey("Ley", on_delete=models.CASCADE)
    articulo = models.TextField()


class Inciso(BaseModel):
    fk_articulo = models.ForeignKey("Articulo", on_delete=models.CASCADE)
    inciso = models.TextField()
