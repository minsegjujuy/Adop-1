from django.db import models
from Operativos.models import Operativo

class TipoServicio(models.Model):
    fk_servicio = models.ForeignKey('Servicio',on_delete=models.CASCADE)
    tipo_servicio = models.TextField()

class Servicio(models.Model):
    fk_operativo = models.ForeignKey(Operativo,on_delete=models.CASCADE)
    cant_recursos = models.IntegerField()
    
class TipoRecurso(models.Model):
    fk_servicio = models.ForeignKey('Servicio',on_delete=models.CASCADE)
    tipo_recurso = models.TextField()
