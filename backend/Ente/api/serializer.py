from rest_framework import serializers
from ..models import Ente


class EnteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ente
        fields = (
            "id",
            "nombre",
            # 'direccion',
        )
        read_only_fields = ("id",)
