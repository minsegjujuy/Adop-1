from django.db import models
from Procedimiento.models import Procedimiento

class TipoSecuestro(models.Model):
    tipo_secuestro = models.CharField(max_length=20)

class Secuestro(models.Model):
    fk_tipo_secuestro = models.ForeignKey('TipoSecuestro',on_delete=models.CASCADE)
    fk_procedimiento = models.ForeignKey(Procedimiento,on_delete=models.CASCADE)
    descripcion = models.TextField()
