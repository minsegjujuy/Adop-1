from django.db import models
from Tableros.settings import URL_ARCHIVOS
from Vigilancia.models import Vigilancia

# Create your models here.
class Documento(models.Model):
    fk_vigilancia = models.ForeignKey(Vigilancia, on_delete=models.CASCADE, blank=False)
    file = models.FileField(upload_to=URL_ARCHIVOS)
    direccion = models.CharField(max_length=255, blank=True, null=True)