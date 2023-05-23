from rest_framework import serializers
from ..models import Jerarquia, Personal, TipoEscalafon, TipoFuncion, TipoJerarquia

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = (
            'legajo',
            'cuil',
            'fk_tipo_funcion',
            'fk_tipo_escalafon',
            'fk_jerarquia',
            'fk_destino',
            'fk_jurisdiccion',
            'domicilio',
            'genero',
            'nombre_apellido',
            'fecha_nacimiento',
            'estado_civil',
            'nacionalidad',
            )
        read_only_fields = ('cuil','legajo')
class TipoFuncionSerializer(serializers.Serializer):
    class Meta:
        model = TipoFuncion
        fields = (
            'id',
            'tipo_funcion',
        )
        read_only_fields = ('tipo_funcion',)

class TipoEscalafonSerializer(serializers.Serializer):
    class Meta:
        model = TipoEscalafon
        fields = (
            'id',
            'tipo_escalafon',
        )
        read_only_fields = ('tipo_escalafon',)

class TipoJerarquiaSerializer(serializers.Serializer):
    class Meta:
        model = TipoJerarquia
        fields = (
            'id',
            'tipo_jerarquia',
        )
        read_only_fields = ('tipo_jerarquia',)

class JerarquiaSerializer(serializers.Serializer):
    class Meta:
        model = Jerarquia
        fields = (
            'id',
            'nombre',
            'sumariante',
            'fk_tipo_jerarquia',
            'nombre_largo',
        )
        read_only_fields = ('nombre', 'sumariante', 'fk_tipo_jerarquia', 'nombre_largo',)
