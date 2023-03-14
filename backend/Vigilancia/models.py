from django.db import models
from Servicio.models import TipoServicio
# from Personal.models import Personal

class Vigilancia(models.Model):
    fk_tipo_servicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)
    comisaria = models.CharField(max_length=50, default='')
    objetivo = models.CharField(max_length=50)
    fecha_inicio = models.DateTimeField(null=False)
    fecha_fin  = models.DateTimeField()
    destino = models.CharField(null=False,max_length=50)
    disposicion = models.CharField(max_length=50)
    longitud = models.DecimalField(decimal_places=10,max_digits=13)
    latitud = models.DecimalField(decimal_places=10,max_digits=13)

class DiasVigilancia(models.Model):
    fk_vigilancia = models.ForeignKey('Vigilancia', on_delete=models.CASCADE)
    dia = models.CharField(null=False,max_length=10)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    dia_completo = models.BooleanField(default=False)