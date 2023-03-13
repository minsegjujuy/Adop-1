from rest_framework import serializers
<<<<<<< HEAD
from users.models import Usuario
=======
from users.models import User, Empleado
>>>>>>> Feature


class UserSerializer(serializers.ModelSerializer):
    class Meta:
<<<<<<< HEAD
        model = Usuario
        fields = [
            'id', 
            'username',
            'email',
            'nombres', 
            'apellidos', 
            'password'
        ]
=======
        model = User
        fields = ['id', 'username', 'email',
                  'first_name', 'last_name', 'password', 'is_active', 'is_staff']


class EmpleadoSerializer(serializers.ModelSerializer):
    User = UserSerializer()

    class Meta:
        model = Empleado
        fields = ["id", "nivel_permiso", "User"]


class SetEmpleadoSerializer(serializers.ModelSerializer):
    User = UserSerializer()

    class Meta:
        model = Empleado
        fields = ["id", "nivel_permiso", "User"]

    # CREACION DE EMPLEADO, LE CREAMOS UN USAURIO UN INDIVIDUO Y SI ES MEDICO LE CREAMOS UN MEDICO

    def create(self, validated_data):

        # Obtenemos datos de usuario
        user_data = validated_data.pop("User")
        usuario = User.objects.create(**user_data)
        empleado = Empleado.objects.create(
            User=usuario, **validated_data
        )
        # si es medico entonces lo creamos
        # if esMedico:
        #     Medico.objects.create(empleado=empleado, **medico_data)
        return empleado
>>>>>>> Feature
