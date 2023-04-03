from rest_framework import serializers
from ..models import Vigilancia, DiasVigilancia

class VigilanciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vigilancia
        fields = (
            'id',
            'regional',
            'motivo',
            'fk_tipo_servicio',
            'objetivo',
            'cant_dias',
            'fecha_inicio',
            'fecha_fin',
            'destino',
            'longitud',
            'latitud',
        )

class DiasVigilanciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiasVigilancia
        fields = (
            'id',
            'fk_vigilancia',
            'fk_personal'
            'dia',
            'hora_inicio',
            'hora_fin',
            'turno',
            'dia_completo'
        )