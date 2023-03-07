from rest_framework import serializers
from ..models import Servicio, TipoRecurso, TipoServicio

class TipoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoServicio
        fields = (
            'id',
            'descripcion',
        )

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = (
            'id',
            'fk_tipo_servicio',
            'fk_operativo',
            'cant_recursos',
        )

class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRecurso
        fields = (
            'id',
            'fk_tipo_servicio',
            'tipo_recurso',
        )