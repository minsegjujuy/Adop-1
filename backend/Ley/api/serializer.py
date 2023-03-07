from rest_framework import serializers
from ..models import Ley, Articulo, Inciso

class LeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ley
        fields = (
            'id',
            'fk_tipo_procedimiento',
            'ley'
        )
        
class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = (
            'id',
            'fk_ley',
            'articulo'
        )
        
class IncisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inciso
        fields = (
            'id',
            'fk_articulo',
            'inciso'
        )