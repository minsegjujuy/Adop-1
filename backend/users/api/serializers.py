from rest_framework import serializers
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import Usuario, Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = [
            'id',
            'rol',
        ]

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'email',
            'nombres',
            'apellidos',
            'rol',
            'jurisdiccion',
            'unidad_regional',
            'is_superuser',
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id', 
            'username',
            'email',
            'nombres', 
            'apellidos',
            'rol',
            'password',
            'jurisdiccion',
            'unidad_regional',
            'is_superuser',
            'usuario_activo'
        ]