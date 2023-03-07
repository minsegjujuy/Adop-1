from django.db import models
from Dependencia.models import Dependencia

# Create your models here.
class Personal(models.Model):
    legajo = models.IntegerField(primary_key=True)
    fk_dependencia = models.ForeignKey(Dependencia,on_delete=models.CASCADE)
    domicilio = models.CharField(max_length=100)
    genero = models.CharField(max_length=8, null=True)
    nombre_apellido = models.CharField(null=False, max_length=80, default='')
    fecha_nacimiento = models.DateTimeField(null=False,default=models.DateField("01/01/1999"))
    estudios = models.CharField(max_length=100)
    oficio = models.CharField(max_length=100)
    jerarquia = models.CharField(max_length=50)
    prestacion_servicios = models.IntegerField(null=False)
    funcion = models.CharField(max_length=100)
    escalafon = models.CharField(max_length=100)
    estado_civil = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    cuil = models.CharField(null=False,max_length=11)