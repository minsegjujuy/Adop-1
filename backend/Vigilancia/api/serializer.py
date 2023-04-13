from rest_framework import serializers
from ..models import Motivo,Vigilancia, DiasVigilancia, TurnoVigilancia

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
            'fk_tipo_servicio',
            'fk_tipo_recurso',
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
            'fecha',
            'hora_inicio',
            'hora_fin',
            'dia_completo'
        )

class TurnoVigilanciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurnoVigilancia
        fields = (
            'id',
            'fk_personal',
            'fk_diaVigilancia',
            'hora_inicio',
            'hora_fin'
        )