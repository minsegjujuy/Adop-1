from rest_framework import serializers
from ..models import Jerarquia, Personal

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = (
            'legajo',
            'fk_persona',
            'fk_jerarquia',
            'fk_destino',
            'fk_jurisdiccion'
        )
        read_only_fields = ('cuil','legajo')

class JerarquiaSerializer(serializers.Serializer):
    class Meta:
        model = Jerarquia
        fields = (
            'id',
            'nombre',
            'nombre_largo',
        )
        read_only_fields = ('id', 'nombre', 'nombre_largo',)
