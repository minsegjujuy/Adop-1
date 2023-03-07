from rest_framework import serializers
from ..models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = (
            'dni',
            'profesion',
            'sexo',
            'nacionalidad',
            'nombre_apellido',
            'edad',
            'fecha_nacimiento'
        )
        read_only_fields = ('dni',)