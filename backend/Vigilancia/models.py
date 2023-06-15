from django.contrib.postgres.fields import ArrayField
from django.db import models
from Servicio.models import TipoRecurso, TipoServicio
from Personal.models import Categoria, Personal
from Dependencia.models import Dependencia, UnidadRegional
from Personal.models import Funcionario

class Ente(Categoria):
    pass

class Motivo(models.Model):
    motivo = models.CharField(max_length=22)

class Archivo(models.Model):
    fk_vigilancia = models.ForeignKey('Vigilancia', on_delete=models.CASCADE)
    path = models.TextField(blank=False)

class Vigilancia(models.Model):
    fk_jurisdiccion = models.ForeignKey(Dependencia, on_delete=models.CASCADE, null=False)
    fk_motivo = models.ForeignKey('Motivo', on_delete=models.CASCADE, null=False)
    fk_tipo_servicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE, null=False)
    fk_tipo_recurso = models.ForeignKey(TipoRecurso, on_delete=models.CASCADE, null=False)
    fk_unidad_regional = models.ForeignKey(UnidadRegional, on_delete=models.CASCADE, null=False)
    
    fk_funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=True, default=None)
    fk_ente = models.ForeignKey(Ente, on_delete=models.CASCADE, null=True, default=None)
    
    objetivo = models.TextField()
    cant_dias = models.IntegerField(default=0)
    fecha_inicio = models.DateTimeField(null=False)
    fecha_fin  = models.DateTimeField(null=True)
    destino = models.CharField(null=False,max_length=50)
    longitud = models.DecimalField(decimal_places=10,max_digits=13)
    latitud = models.DecimalField(decimal_places=10,max_digits=13)
    turno_asignado = models.BooleanField(default=False)
    # activar luego de la primera migracion
    # turnos_vigilancias = models.ManyToManyField('TurnosVigilancia', db_table='vigilancia_turnosvigilancia', related_name='turnosvigilancia', default=None) #comentar para la primera migracion
    
    # def save(self, *args, **kwargs):
    #     with open('BaseDeDatos/script_triggers.sql', encoding='utf-8') as sql_script:
    #         sql = sql_script.read()
    #     print(sql)
    #     with connections['default'].cursor() as cursor:
    #         cursor.execute(sql)

class TurnosVigilancia(models.Model):
    fk_vigilancia = models.ForeignKey('Vigilancia', on_delete=models.CASCADE)
    turno = ArrayField(models.TextField())
    hora_inicio = models.TimeField(null=True)
    hora_fin = models.TimeField(null=True)
    diario = models.BooleanField(default=False)
    dia_completo = models.BooleanField(default=False)
    duracion = models.IntegerField(default=0,null=True)

class PersonalVigilancia(models.Model):
    fk_personal = models.ForeignKey(Personal, null=True, on_delete=models.CASCADE)
    fk_turnoVigilancia = models.ForeignKey('TurnosVigilancia', on_delete=models.CASCADE)
    fecha = models.DateField(null=False)
    hora_inicio = models.TimeField(null=False)
    hora_fin = models.TimeField(null=False)
    duracion = models.IntegerField(null=False)
    asignado = models.BooleanField(default=False)