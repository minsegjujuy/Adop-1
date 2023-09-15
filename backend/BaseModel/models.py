from datetime import datetime
from django.db import models


class BaseModel(models.Model):
    usuario_alta = models.IntegerField(null=True, blank=True, default=None)
    usuario_modificacion = models.IntegerField(null=True, blank=True, default=None)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)
    is_deleted = models.BooleanField(default=False)

    def persist(self, usuario=None, *args, **kwargs):
        if usuario.is_authenticated:
            self.usuario_modificacion = usuario.id
        self.updated_at = datetime.now().isoformat()
        self.save()

    def new_save(self, usuario=None, *args, **kwargs):
        if usuario.is_authenticated:
            self.usuario_alta = usuario.id
        self.created_at = datetime.now().isoformat()
        self.persist(usuario=usuario, *args, **kwargs)

    def softDelete(self, usuario=None, *args, **kwargs):
        self.is_deleted = True
        self.deleted_at = datetime.now().isoformat()
        self.persist(usuario=usuario, *args, **kwargs)

    def softRestore(self, usuario=None, *args, **kwargs):
        self.is_deleted = False
        self.deleted_at = None
        self.persist(usuario=usuario, *args, **kwargs)

    class Meta:
        abstract = True
