from rest_framework import serializers
from ..models import Documento


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = ("id", "file", "nombre", "fk_vigilancia")
        read_only_fields = ("id",)
