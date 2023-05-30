from rest_framework import serializers
from ..models import Motivo,Vigilancia, TurnosVigilancia, PersonalVigilancia

class MotivoVigilanciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motivo
        fields = (
            'id',
            'motivo'
        )

class VigilanciaSerializerView(serializers.ModelSerializer):
    class Meta:
        model = Vigilancia
        fields = (
            'id',
            'fk_jurisdiccion',
            'fk_motivo',
            'fk_tipo_servicio',
            'fk_tipo_recurso',
            'fk_unidad_regional',
            'objetivo',
            'cant_dias',
            'fecha_inicio',
            'fecha_fin',
            'turno_asignado',
            'destino',
            'longitud',
            'latitud',
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
            'fk_unidad_regional',
            'objetivo',
            'cant_dias',
            'fecha_inicio',
            'fecha_fin',
            'destino',
            'longitud',
            'latitud',
        )

class TurnosVigilanciaSerializerView(serializers.ModelSerializer):
    class Meta:
        model = TurnosVigilancia
        fields = (
            'id',
            'fk_vigilancia',
            'turno',
            'hora_inicio',
            'hora_fin',
            'duracion',
            'diario',
            'dia_completo'
        )

class TurnosVigilanciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurnosVigilancia
        fields = (
            'id',
            'fk_vigilancia',
            'turno',
            'hora_inicio',
            'hora_fin',
            'diario',
            'dia_completo'
        )

class PersonalVigilanciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalVigilancia
        fields = (
            'id',
            'fk_personal',
            'fk_turnoVigilancia',
            'fecha',
            'hora_inicio',
            'hora_fin',
            'duracion',
            'asignado'
        )