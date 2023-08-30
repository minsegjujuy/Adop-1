from datetime import timezone
from datetime import datetime
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    usuario_alta = models.IntegerField(null=True, blank=True)
    usuario_modificacion = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)
    is_deleted = models.BooleanField(default=False)
    
    def save(self, usuario=None):
        self.usuario_modificacion = usuario
        self.updated_at = datetime.now
        super().save()
    
    def new_save(self, usuario=None):
        self.created_at = datetime.now
        self.usuario_alta = usuario
        self.save()

    def softDelete(self, usuario=None):
        self.is_deleted = True
        self.deleted_at = datetime.now().isoformat()
        self.save()

    def softRestore(self, usuario=None):
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True
