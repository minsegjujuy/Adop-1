from django.db import models
from Dependencia.models import Dependencia, UnidadRegional
from Persona.models import Persona

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True, null=True)
    
    def activar(self):
        self.activo = True
        
    def desactivar(self):
        self.activo = False

    class Meta:
        abstract = True

class Jerarquia(Categoria):
    nombre_largo = models.CharField(max_length=255)

class Personal(models.Model):
    legajo = models.IntegerField(primary_key=True)
    fk_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, default=None)
    # fk_tipo_funcion = models.ForeignKey('TipoFuncion', on_delete=models.CASCADE)
    fk_jerarquia = models.ForeignKey('Jerarquia', on_delete=models.CASCADE)
    fk_destino = models.ForeignKey(Dependencia, on_delete=models.CASCADE, null=True)
    fk_jurisdiccion = models.ForeignKey(UnidadRegional, on_delete=models.CASCADE, null=True)
    
class Cargo(Categoria):
    pass

class Funcionario(models.Model):
    fk_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fk_cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE)
    fecha_inicio = models.DateField(null=False)
    fecha_fin = models.DateField(null=True)