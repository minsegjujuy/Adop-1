from django.db import models
from Operativos.models import Operativo

class TipoServicio(models.Model):
    tipo_servicio = models.TextField()
    
class TipoRecurso(models.Model):
    tipo_recurso = models.TextField()

class Servicio(models.Model):
    fk_operativo = models.ForeignKey(Operativo,on_delete=models.CASCADE)
    fk_tipo_servicio = models.ForeignKey('TipoServicio',on_delete=models.CASCADE, null=True)
    fk_tipo_recurso = models.ForeignKey('TipoRecurso',on_delete=models.CASCADE, null=True)
    cant_recursos = models.IntegerField()
