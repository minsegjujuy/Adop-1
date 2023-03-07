from django.db import models

class Persona(models.Model):
    dni = models.BigIntegerField(primary_key=True)
    profesion = models.CharField(max_length=100)
    sexo = models.CharField(max_length=8)
    nacionalidad = models.CharField(max_length=100)
    nombre_apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateTimeField(null=False)
