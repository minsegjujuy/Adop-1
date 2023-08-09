from rest_framework import serializers
from ..models import Persona


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = (
            "cuil",
            "dni",
            "nombre_apellido",
            "fecha_nacimiento",
        )
        read_only_fields = ("dni",)
