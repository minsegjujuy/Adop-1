from rest_framework import serializers
from ..models import Dependencia, Inspectora, UnidadRegional, DependenciaOperativos

class InspectoraSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Inspectora
        fields = (
            'id',
        )
        read_only_fields = ('id',)
        
class UnidadRegionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadRegional
        fields = (
            'id',
            'unidad_regional',
        )
        read_only_fields = ('id',)

class DependenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependencia
        fields = (
            'id',
            'fk_unidad_regional',
            'fk_inspectora',
            'jurisdiccion',
            )
        read_only_fields = ('id',)

class DependenciaOperativosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DependenciaOperativos
        fields = (
            'id',
            'fk_dependencia',
            'fk_operativo',
        )
        read_only_fields = ('id',)