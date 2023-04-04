from rest_framework import serializers
from ..models import Motivo,Vigilancia, DiasVigilancia

class MotivoVigilanciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motivo
        fields = (
            'id',
            'motivo'
        )

class VigilanciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vigilancia
        fields = (
            'id',
            'fk_jurisdiccion',
            'fk_motivo',
            'fk_servicio',
            'regional',
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