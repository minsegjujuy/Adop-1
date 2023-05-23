from django.db import models
from Dependencia.models import Dependencia, UnidadRegional

class TipoFuncion(models.Model):
    tipo_funcion = models.CharField(max_length=100)

class TipoEscalafon(models.Model):
    tipo_escalafon = models.CharField(max_length=100)

class TipoJerarquia(models.Model):
    tipo_jerarquia = models.CharField(max_length=100)
    
class Jerarquia(models.Model):
    nombre = models.CharField(max_length=100)
    sumariante = models.BooleanField(default=False)
    fk_tipo_jerarquia = models.ForeignKey('TipoJerarquia',on_delete=models.CASCADE)
    nombre_largo = models.CharField(max_length=255)

# Create your models here.
class Personal(models.Model):
    legajo = models.IntegerField(primary_key=True)
    cuil = models.CharField(null=False,max_length=11, unique=True)
    fk_tipo_funcion = models.ForeignKey('TipoFuncion', on_delete=models.CASCADE)
    fk_tipo_escalafon = models.ForeignKey('TipoEscalafon', on_delete=models.CASCADE)
    fk_jerarquia = models.ForeignKey('Jerarquia', on_delete=models.CASCADE)
    fk_destino = models.ForeignKey(Dependencia, on_delete=models.CASCADE)
    fk_jurisdiccion = models.ForeignKey(UnidadRegional, on_delete=models.CASCADE)
    domicilio = models.CharField(max_length=100)
    genero = models.CharField(max_length=8, null=True)
    nombre_apellido = models.CharField(null=False, max_length=80, default='')
    fecha_nacimiento = models.DateTimeField(null=False,default=models.DateField("01/01/1999"))
    estado_civil = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)