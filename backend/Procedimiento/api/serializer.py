from rest_framework import serializers
from ..models import Procedimiento, ProcedimientoPersona

class ProcedimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedimiento
        fields = (
            'id',
            'fk_servicio',
            'description',
            'hora',
            'latitud',
            'longitud',
            'cant_protagonistas',
            'cant_infracciones',
            'cant_arrestados',
            )
        # read_only_fields = ('latitud','longitud')

class ProcedimientoPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcedimientoPersona
        flieds = (
            'id',
            'fk_procedimiento',
            'fk_persona',
            'detenido',
        )