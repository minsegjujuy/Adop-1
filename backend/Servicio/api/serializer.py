from rest_framework import serializers
from ..models import Servicio, TipoRecurso, TipoServicio


class TipoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoServicio
        fields = (
            "id",
            "tipo_servicio",
        )


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = (
            "id",
            "fk_tipo_servicio",
            "fk_tipo_recurso",
            "fk_operativo",
            "cant_recursos",
        )


class TipoRecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRecurso
        fields = (
            "id",
            "tipo_recurso",
        )
