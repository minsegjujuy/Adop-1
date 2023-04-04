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
<<<<<<< HEAD
            'jurisdiccion',
=======
            'jurisdiccion'
>>>>>>> 1cedd5633c1a7c8c2fbb9e517314aa5d326b4513
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