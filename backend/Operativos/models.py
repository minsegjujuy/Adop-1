from django.db import models
from Personal.models import Personal
from Dependencia.models import Dependencia
from BaseModel.models import BaseModel
from auditlog.registry import auditlog


# Create your models here.
class Operativo(BaseModel):
    jefe_cargo = models.IntegerField()
    hora_inicio = models.TimeField(null=False)
    hora_final = models.TimeField(null=False)
    jurisdiccion = models.ForeignKey(Dependencia, on_delete=models.CASCADE, null=True)
    fecha = models.DateField(null=False)
    latitud = models.DecimalField(null=False, decimal_places=10, max_digits=13)
    longitud = models.DecimalField(null=False, decimal_places=10, max_digits=13)
    cant_personas_afectadas = models.IntegerField(null=False)
    cant_recursos = models.IntegerField(null=False)
    procedimiento = models.BooleanField(null=False)
    turno = models.CharField(null=False, max_length=10)
    # activar luego de la primera migracion
    # personal = models.ManyToManyField('OperativoPersonal', db_table='operativo_personal', related_name='personal') #comentar para la primera migracion


class OperativoPersonal(BaseModel):
    fk_operativo = models.ForeignKey("Operativos.Operativo", on_delete=models.CASCADE)
    fk_personal = models.ForeignKey(Personal, on_delete=models.CASCADE)


auditlog.register(
    Operativo,
    exclude_fields=[
        "updated_at",
        "created_at",
        "deleted_at",
    ],
)
auditlog.register(
    OperativoPersonal,
    exclude_fields=[
        "updated_at",
        "created_at",
        "deleted_at",
    ],
)
