from django.db import models

from SoftDelete.models import SoftDeleteModel
from users.models import Usuario

class Note(SoftDeleteModel):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="notes", null=True)
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=255)