from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import Usuario

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'email',
            'nombres',
            'apellidos',
            'rol',
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
            'password',
            'rol',
            'is_superuser',
            'usuario_activo'
        ]
        