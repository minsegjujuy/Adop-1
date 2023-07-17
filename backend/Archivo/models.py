from django.db import models

# Create your models here.
class Documento(models.Model):
    archivo = models.FileField(upload_to='archivos/vigilancias/')
    direccion = models.CharField(max_length=255, blank=True, null=True)