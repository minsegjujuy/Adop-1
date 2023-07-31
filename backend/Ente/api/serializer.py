from rest_framework import serializers
from ..models import Documento

class EnteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = (
            'id',
            'nombre',
            # 'direccion',
        )
        read_only_fields = ('id',)