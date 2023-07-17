from rest_framework import serializers
from ..models import Documento

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = (
            'id',
            'archivo',
        )
        read_only_fields = ('id',)