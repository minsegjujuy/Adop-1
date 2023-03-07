from rest_framework import serializers
from ..models import Operativo, OperativoPersonal

class OperativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operativo
        fields = (
            'id',
            'jefe_cargo',
            'hora_inicio',
            'dependenciaOP',
            'hora_final',
            'fecha',
            'latitud',
            'longitud',
            'cant_personas_afectadas',
            'cant_recursos',
            'procedimiento',
            'turno',
            'personal'
        )
        # read_only_fields = ('id',)
        
class OperativoPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperativoPersonal
        fields = (
            'id',
            'fk_operativo',
            'fk_personal',
        )
        # read_only_fields = ('id',)