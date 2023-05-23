from django.db import models
from Dependencia.models import Dependencia, UnidadRegional

# class TipoFuncion(models.Model):
    # tipo_funcion = models.CharField(max_length=100)
    
class Jerarquia(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_largo = models.CharField(max_length=255)

class Personal(models.Model):
    legajo = models.IntegerField(primary_key=True)
    cuil = models.BigIntegerField(null=False)
    # fk_tipo_funcion = models.ForeignKey('TipoFuncion', on_delete=models.CASCADE)
    fk_jerarquia = models.ForeignKey('Jerarquia', on_delete=models.CASCADE)
    fk_destino = models.ForeignKey(Dependencia, on_delete=models.CASCADE, null=True)
    fk_jurisdiccion = models.ForeignKey(UnidadRegional, on_delete=models.CASCADE, null=True)