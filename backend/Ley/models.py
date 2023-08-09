from django.db import models
from Procedimiento.models import TipoProcedimiento


class Ley(models.Model):
    fk_tipo_procedimiento = models.ForeignKey(TipoProcedimiento, on_delete=models.CASCADE)
    ley = models.TextField()


class Articulo(models.Model):
    fk_ley = models.ForeignKey("Ley", on_delete=models.CASCADE)
    articulo = models.TextField()


class Inciso(models.Model):
    fk_articulo = models.ForeignKey("Articulo", on_delete=models.CASCADE)
    inciso = models.TextField()
