from django.contrib.postgres.fields import ArrayField
from django.db import models
from Servicio.models import TipoRecurso, TipoServicio
from Personal.models import Personal
from Dependencia.models import Dependencia, UnidadRegional
from Personal.models import Funcionario
from Ente.models import Ente
from BaseModel.models import BaseModel
from auditlog.registry import auditlog


class Motivo(BaseModel):
    motivo = models.CharField(max_length=22, unique=True)


class Vigilancia(BaseModel):
    fk_jurisdiccion = models.ForeignKey(
        Dependencia, on_delete=models.CASCADE, null=False
    )
    fk_motivo = models.ForeignKey("Motivo", on_delete=models.CASCADE, null=False)
    fk_tipo_servicio = models.ForeignKey(
        TipoServicio, on_delete=models.CASCADE, null=False
    )
    # fk_tipo_recurso = models.ForeignKey(TipoRecurso, on_delete=models.CASCADE, null=False)
    # fk_recursos = ArrayField(models.IntegerField(TipoRecurso, null=False), null=False, default=[])
    fk_unidad_regional = models.ForeignKey(
        UnidadRegional, on_delete=models.CASCADE, null=False
    )

    fk_funcionario = models.ForeignKey(
        Funcionario, on_delete=models.CASCADE, null=True, default=None
    )
    fk_ente = models.ForeignKey(Ente, on_delete=models.CASCADE, null=True, default=None)

    objetivo = models.TextField()
    cant_dias = models.IntegerField(default=0)
    fecha_inicio = models.DateTimeField(null=False)
    fecha_fin = models.DateTimeField(null=True)
    destino = models.CharField(null=False, max_length=50)
    longitud = models.DecimalField(decimal_places=10, max_digits=13)
    latitud = models.DecimalField(decimal_places=10, max_digits=13)
    turno_asignado = models.BooleanField(default=False)
    # activar luego de la primera migracion
    # turnos_vigilancias = models.ManyToManyField('TurnosVigilancia', db_table='vigilancia_turnosvigilancia', related_name='turnosvigilancia', default=None) #comentar para la primera migracion


class RecursosVigilancia(BaseModel):
    fk_tipo_recurso = models.ForeignKey(
        TipoRecurso, on_delete=models.CASCADE, null=False
    )
    fk_vigilancia = models.ForeignKey(
        "Vigilancia", on_delete=models.CASCADE, null=False
    )
    cantidad = models.IntegerField(null=False, default=0)
    fecha = models.DateField(null=False)


class TurnosVigilancia(BaseModel):
    fk_vigilancia = models.ForeignKey("Vigilancia", on_delete=models.CASCADE)
    turno = ArrayField(models.TextField())
    hora_inicio = models.TimeField(null=True)
    hora_fin = models.TimeField(null=True)
    diario = models.BooleanField(default=False)
    dia_completo = models.BooleanField(default=False)
    duracion = models.IntegerField(default=0, null=True)


class PersonalVigilancia(BaseModel):
    fk_personal = models.ForeignKey(Personal, null=True, on_delete=models.CASCADE)
    fk_turnoVigilancia = models.ForeignKey("TurnosVigilancia", on_delete=models.CASCADE)
    fecha = models.DateField(null=False)
    hora_inicio = models.TimeField(null=False)
    hora_fin = models.TimeField(null=False)
    duracion = models.IntegerField(null=False)
    asignado = models.BooleanField(default=False)


auditlog.register(
    Motivo,
    exclude_fields=[
        "updated_at",
        "created_at",
        "deleted_at",
    ],
)
auditlog.register(
    Vigilancia,
    exclude_fields=[
        "updated_at",
        "created_at",
        "deleted_at",
    ],
)
auditlog.register(
    RecursosVigilancia,
    exclude_fields=[
        "updated_at",
        "created_at",
        "deleted_at",
    ],
)
auditlog.register(
    TurnosVigilancia,
    exclude_fields=[
        "updated_at",
        "created_at",
        "deleted_at",
    ],
)
auditlog.register(
    PersonalVigilancia,
    exclude_fields=[
        "updated_at",
        "created_at",
        "deleted_at",
    ],
)
