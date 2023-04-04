from django.db import models
from Servicio.models import Servicio
from Personal.models import Personal
from Dependencia.models import Dependencia

class Motivo(models.Model):
    motivo = models.CharField(max_length=22)

class Vigilancia(models.Model):
    fk_jurisdiccion = models.ForeignKey(Dependencia, on_delete=models.CASCADE)
    fk_motivo = models.ForeignKey('Motivo', on_delete=models.CASCADE, null=True)
    fk_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=True)
    regional = models.CharField(max_length=50, default='')
    objetivo = models.TextField()
    cant_dias = models.IntegerField(default=0, blank=True)
    fecha_inicio = models.DateTimeField(null=False)
    fecha_fin  = models.DateTimeField(null=True)
    destino = models.CharField(null=False,max_length=50)
    longitud = models.DecimalField(decimal_places=10,max_digits=13)
    latitud = models.DecimalField(decimal_places=10,max_digits=13)
class DiasVigilancia(models.Model):
    fk_vigilancia = models.ForeignKey('Vigilancia', on_delete=models.CASCADE)
    fk_personal = models.ForeignKey(Personal, on_delete=models.CASCADE, null=True)
    dia = models.DateTimeField(null=False)
    hora_inicio = models.TimeField(null=True)
    hora_fin = models.TimeField(null=True)
    turno = models.CharField(max_length=100,null=True)
    dia_completo = models.BooleanField(default=False)