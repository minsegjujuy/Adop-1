from rest_framework import serializers
from ..models import TipoSecuestro, Secuestro

class TipoSecuestroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSecuestro
        fields = (
            'id',
            'tipo_secuestro',
        )

class SecuestroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secuestro
        fields = (
            'id',
            'fk_tipo_secuestro',
            'fk_procedimiento',
            'descripcion',
        )
        read_only_fields = ('dni',)