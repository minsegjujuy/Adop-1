from django.db import models
from Vigilancia.models import Vigilancia
from BaseModel.models import BaseModel
from auditlog.registry import auditlog


def directorio_dinamico(instance, filename):
    # Aquí puedes construir la ruta dinámica basada en la instancia del modelo y el nombre del archivo
    return f"vigilancias/vigilancia-{instance.fk_vigilancia.id}/{instance.nombre}"


# Create your models here.
class Documento(BaseModel):
    fk_vigilancia = models.ForeignKey(Vigilancia, on_delete=models.CASCADE, blank=False)
    nombre = models.CharField(max_length=100, default="")
    file = models.FileField(upload_to=directorio_dinamico)


auditlog.register(
    Documento,
    exclude_fields=[
        "updated_at",
        "created_at",
        "deleted_at",
    ],
)
