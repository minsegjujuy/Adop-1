from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
<<<<<<< HEAD
from users.models import Usuario
=======
from rest_framework import status
from users.models import User, Empleado
>>>>>>> Feature
from users.api.serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permisos import (
    PermisoAdministrador,
    PermisoOperador,
    PermisoFarmaceutico,
)
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from django.contrib.auth.hashers import make_password
from users.api.serializers import (EmpleadoSerializer, SetEmpleadoSerializer)


class UserApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = Usuario.objects.all()

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        password = request.data['password']

        if password:
            request.data['password'] = make_password(password)
        else:
            request.data['password'] = request.user.password
        return super().update(request, *args, **kwargs)


class UserView (APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class EmpleadoApiViewSet(ModelViewSet):
    permission_class = [IsAuthenticated]
    permission_class = [PermisoAdministrador]
    serializer_class = SetEmpleadoSerializer
    queryset = Empleado.objects.all()
    filter_backends = [DjangoFilterBackend]

    def create(self, request, *args, **kwargs):
        request.data["User"]["password"] = make_password(
            request.data["User"]["password"]
        )
        print(request.data["User"]["password"])
        return super().create(request, *args, **kwargs)


class EmpleadoCreateAPIView(CreateAPIView):
    permission_class = [IsAuthenticated]
    permission_class = [PermisoAdministrador]
    serializer_class = EmpleadoSerializer

    def create(self, request, *args, **kwargs):
        serializer = EmpleadoSerializer(
            data=request.data, context={"request": request})
        if serializer.is_valid():

            # Obtenemos datos de usuario y lo creamos
            user_data = serializer.validated_data.pop("User")
            contrasenia = make_password(user_data.pop("password"))
            usuario = User.objects.create(password=contrasenia, **user_data)

            # obtenemos el id del individuo

            empleado = Empleado.objects.create(
                User=usuario, **serializer.validated_data
            )

            empleado.save()

            return Response(
                {"msj": "Empleado creado correctamente"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpleadoUsuarioIdListApiView(ListAPIView):
    permission_class = [IsAuthenticated]
    permission_class = [PermisoAdministrador]
    serializer_class = SetEmpleadoSerializer

    def get_queryset(self):
        id_usuario = self.kwargs["id_usuario"]
        if Empleado.objects.filter(User_id=id_usuario).exists():
            return Empleado.objects.filter(User_id=id_usuario)
