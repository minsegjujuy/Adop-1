from django.contrib.auth import authenticate
from django.contrib.sessions.models import Session
from django.http import JsonResponse

from Dependencia.models import Dependencia, UnidadRegional
from BaseModel.api.views import DynamicModelViewSet

from users.models import Usuario, Rol
from users.api.serializers import UserSerializer, TokenSerializer, RolSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import action

from rest_framework.response import Response

from rest_framework.authtoken.models import Token

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

import datetime

from ..authentication_mixins import Authentication


class RolViewSet(Authentication, DynamicModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class UserViewSet(Authentication, DynamicModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=["put"])
    def update(self, request, pk=None):
        usuario = self.get_object(pk)
        serializer = UserSerializer(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            usuario = Usuario(**serializer.validated_data)
            usuario.save(request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["patch"])
    def partial_update(self, request, pk=None):
        user_id = pk
        if user_id:
            usuario = Usuario.objects.get(id=user_id)

            username = request.data.get("username")
            if username:
                usuario.username = username

            email = request.data.get("email")
            if email:
                usuario.email = email

            nombres = request.data.get("nombres")
            if nombres:
                usuario.nombres = nombres

            apellidos = request.data.get("apellidos")
            if apellidos:
                usuario.apellidos = apellidos

            old_password = request.data.get("old_password")
            new_password = request.data.get("new_password")
            if old_password and new_password:
                if usuario.check_password(old_password):
                    usuario.set_password(new_password)
                else:
                    return Response(
                        {"msj": "La contrasenia ingresada es incorrecta"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            rol = request.data.get("rol")
            if rol:
                usuario.rol = Rol.objects.get(id=rol)

            jurisdiccion = request.data.get("jurisdiccion")
            if jurisdiccion:
                usuario.jurisdiccion = Dependencia.objects.get(id=jurisdiccion)

            unidad_regional = request.data.get("unidad_regional")
            if unidad_regional:
                usuario.unidad_regional = UnidadRegional.objects.get(id=unidad_regional)

            admin = request.data.get("is_superuser")
            if admin:
                usuario.is_superuser = admin
                usuario.rol = Rol.objects.get(id=1)
                usuario.jurisdiccion = None
                usuario.unidad_regional = None

            usuario.save(request.user)
            respuesta = {"msj": "Usuario Actualizado Correctamente!!"}
            return Response(respuesta, status=status.HTTP_200_OK)
        else:
            respuesta = {"msj": "No se ingreso el id del usuario a modificar"}
            return Response(respuesta, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["post"])
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        datos = serializer.validated_data
        username = datos.get("username")
        email = datos.get("email")
        password = datos.get("password")
        is_superuser = datos.get("is_superuser")
        if is_superuser:
            Usuario.objects.create_superuser(username, email, 1, password)
        else:
            Usuario.objects.create_user(
                email=email,
                username=username,
                nombres=datos["nombres"],
                apellidos=datos["apellidos"],
                rol=datos["rol"],
                unidad_regional=datos["unidad_regional"],
                jurisdiccion=datos["jurisdiccion"],
                password=password,
                is_superuser=False,
            )

        respuesta = {"msj": "Usuario creado Correctamente!!"}

        response = JsonResponse(respuesta, safe=False)

        return response


class RefreshToken(APIView):
    def get(slef, request, *args, **kwargs):
        username = request.GET.get("username")
        try:
            user_token = Token.objects.get(
                user=TokenSerializer()
                .Meta.model.objects.filter(username=username)
                .first()
            )
            return Response({"token": user_token.key})
        except:
            return Response(
                {"error": "Credenciales Enviadas Incorrectas"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class Login(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            user = authenticate(email=email, password=password)
            if user:
                if user.usuario_activo:
                    login_serializer = self.serializer_class(data=request.data)
                    if login_serializer.is_valid:
                        token, created = Token.objects.get_or_create(user=user)
                        user_data = UserSerializer(user).data
                        if created:
                            return Response(
                                {
                                    "token": token.key,
                                    "usuario": TokenSerializer(user).data,
                                    "message": "Inicio de Sesion Exitoso",
                                },
                                status=status.HTTP_200_OK,
                            )
                        else:
                            all_sessions = Session.objects.filter(
                                expire_date__gte=datetime.datetime.now()
                            )
                            if all_sessions.exists():
                                for session in all_sessions:
                                    session_data = session.get_decoded()
                                    if user_data["id"] == (
                                        session_data.get("_auth_user_id")
                                    ):
                                        session.delete()
                            token.delete()
                            token = Token.objects.create(user=user)
                            usuario = TokenSerializer(user).data
                            datos = {}
                            datos["username"] = usuario["username"]
                            datos["email"] = usuario["email"]
                            datos["nombres"] = usuario["nombres"]
                            datos["apellidos"] = usuario["apellidos"]
                            datos["rol"] = Rol.objects.get(id=usuario["rol"]).id
                            datos["jurisdiccion"] = usuario["jurisdiccion"]
                            datos["unidad_regional"] = usuario["unidad_regional"]
                            # datos['is_superuser'] = usuario['is_superuser']
                            return Response(
                                {
                                    "token": token.key,
                                    "usuario": datos,
                                    "mensaje": "inicio de Sesion Existoso",
                                },
                                status=status.HTTP_200_OK,
                            )
                    return Response(
                        {"error": "Contrasenia o Email incorrectos"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                return Response(
                    {"error": "Este usuario no puede iniciar sesion."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            return Response(
                {"error": "Contrasenia o Email incorrectos"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except:
            return Response(
                {"error": "Error de Busqueda de Usuario"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class Logout(APIView):
    def post(self, request, *args, **kwargs):
        try:
            token = Token.objects.filter(key=request.POST["token"]).first()
            if token:
                user = token.user
                all_sessions = Session.objects.filter(
                    expire_date__gte=datetime.datetime.now()
                )
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == (session_data.get("_auth_user_id")):
                            session.delete()

                token.delete()

                return Response(
                    {
                        "token_message": "Token Eliminado",
                        "session_message": "Sesiones de Usuario Eliminadas",
                    },
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"error": "No se ha encontrado un usuario con estas credenciales."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except:
            return Response(
                {"error": "No se ha encontrado token en la peticion"},
                status=status.HTTP_409_CONFLICT,
            )
