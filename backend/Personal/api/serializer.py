from rest_framework import serializers
from ..models import Personal

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = (
            'legajo',
            'cuil',
            'fk_dependencia',
            'domicilio',
            'genero',
            'estudios',
            'oficio',
            'jerarquia',
            'prestacion_servicios',
            'funcio',
            'escalafon',
            'nombre_apellido',
            'fecha_nacimiento',
            'estado_civil',
            'nacionalidad'
            )
        read_only_fields = ('cuil','legajo')