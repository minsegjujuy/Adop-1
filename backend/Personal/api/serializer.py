from rest_framework import serializers
from ..models import Cargo, Funcionario, Jerarquia, Personal

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = (
            'legajo',
            'fk_persona',
            'fk_jerarquia',
            'fk_destino',
            'fk_jurisdiccion'
        )
        read_only_fields = ('cuil','legajo')

class JerarquiaSerializer(serializers.Serializer):
    class Meta:
        model = Jerarquia
        fields = (
            'id',
            'nombre',
            'nombre_largo',
            'activo',
        )
        read_only_fields = ('id', 'nombre', 'nombre_largo',)

class FuncionarioSerializer(serializers.Serializer):
    class Meta:
        model = Funcionario
        fields = (
            'fk_persona',
            'fk_cargo',
            'fecha_inicio',
            'fecha_fin'
        )

class CargoSerializer(serializers.Serializer):
    class Meta:
        model = Cargo
        fields = (
            'id',
            'nombre',
            'activo',
        )
        read_only_fields = ('id', 'nombre',)
