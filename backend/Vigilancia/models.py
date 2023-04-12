from django.db import models
from Servicio.models import TipoRecurso, TipoServicio
from Personal.models import Personal
from Dependencia.models import Dependencia

class Motivo(models.Model):
    motivo = models.CharField(max_length=22)

class Vigilancia(models.Model):
    fk_jurisdiccion = models.ForeignKey(Dependencia, on_delete=models.CASCADE)
    fk_motivo = models.ForeignKey('Motivo', on_delete=models.CASCADE, null=True)
    fk_tipo_servicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE, null=True)
    fk_tipo_recurso = models.ForeignKey(TipoRecurso, on_delete=models.CASCADE, null=True)
    regional = models.CharField(max_length=50, default='')
    objetivo = models.TextField()
    cant_dias = models.IntegerField(default=0)
    fecha_inicio = models.DateTimeField(null=False)
    fecha_fin  = models.DateTimeField(null=True)
    destino = models.CharField(null=False,max_length=50)
    longitud = models.DecimalField(decimal_places=10,max_digits=13)
    latitud = models.DecimalField(decimal_places=10,max_digits=13)
    # activar luego de la primera migracion
    # dias_vigilancias = models.ManyToManyField('DiasVigilancia', db_table='vigilancia_diasvigilancia', related_name='dias_vigilancias') #comentar para la primera migracion
    
    # def save(self, *args, **kwargs):
    #     with open('BaseDeDatos/script_triggers.sql', encoding='utf-8') as sql_script:
    #         sql = sql_script.read()
    #     print(sql)
    #     with connections['default'].cursor() as cursor:
    #         cursor.execute(sql)

class DiasVigilancia(models.Model):
    fk_vigilancia = models.ForeignKey('Vigilancia', on_delete=models.CASCADE)
    fecha = models.DateTimeField(null=False)
    hora_inicio = models.TimeField(null=True)
    hora_fin = models.TimeField(null=True)
    dia_completo = models.BooleanField(default=False)

class TurnoVigilancia(models.Model):
    fk_personal = models.ForeignKey(Personal, null=False, on_delete=models.CASCADE)
    fk_diaVigilancia = models.ForeignKey('DiasVigilancia', on_delete=models.CASCADE)
    hora_inicio = models.TimeField(null=False)
    hora_fin = models.TimeField(null=False)