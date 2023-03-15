from rest_framework import serializers
from ..models import Vigilancia, DiasVigilancia

class VigilanciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vigilancia
        fields = (
            'id',
            'fk_tipo_servicio',
            'objetivo',
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
            'dia',
            'hora_inicio',
            'hora_fin',
            'dia_completo'
        )