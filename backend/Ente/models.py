from django.db import models

class Ente(models.Model):
    nombre = models.CharField(max_length=150)
    # direccion = models.CharField(max_length=255)