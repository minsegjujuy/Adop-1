from rest_framework import serializers
from users.models import Usuario


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id', 
            'username',
            'email',
            'nombres', 
            'apellidos', 
            'password'
        ]
