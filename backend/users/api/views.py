from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.sessions.models import Session
from django.http import JsonResponse

from users.models import Usuario, Rol
from users.api.serializers import UserSerializer, TokenSerializer, RolSerializer

from rest_framework import status, viewsets
from rest_framework.views import APIView

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.response import Response

from rest_framework.authtoken.models import Token

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

import datetime

from ..authentication_mixins import Authentication

class RolViewSet(Authentication, viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,IsAuthenticated)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Rol.objects.all()  
    serializer_class = RolSerializer

class UserViewSet(Authentication,viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,IsAuthenticated)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Usuario.objects.all()  
    serializer_class = UserSerializer
    
    def partial_update(self, request, *args, **kwargs):
        password = request.data['password']

        if password:
            request.data['password'] = make_password(password)
        else:
            request.data['password'] = request.user.password
        return super().update(request, *args, **kwargs)
    
    def create(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        username = serializer.validated_data.get('username')
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        nombres = serializer.validated_data.get('nombres')
        apellidos = serializer.validated_data.get('apellidos')
        rol = serializer.validated_data.get('rol')
        jurisdiccion = serializer.validated_data.get('jurisdiccion')
        regional = serializer.validated_data.get('regional')
        is_superuser = serializer.validated_data.get('is_superuser')
        
        usuario = Usuario.objects.create_user(
                        email=email,
                        username=username,
                        nombres=nombres,
                        apellidos=apellidos,
                        rol=rol,
                        unidad_regional=regional,
                        jurisdiccion=jurisdiccion,
                        password=password,
                        is_superuser=is_superuser)
        
        data = {
            'id':usuario.id, 
            'username':usuario.username,
            'email':usuario.email,
            'nombres':usuario.nombres, 
            'apellidos':usuario.apellidos,
            'rol':usuario.rol,
            'jurisdiccion':usuario.jurisdiccion,
            'regional':usuario.regional,
            'is_superuser':usuario.is_superuser,
            'usuario_activo':usuario.usuario_activo
        }
        
        response = JsonResponse(data, safe=False)
        
        return response
    
class RefreshToken(APIView):
    def get(slef,request,*args, **kwargs):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(
                user=TokenSerializer().Meta.model.objects.filter(username=username).first()
            )
            return Response({
                'token': user_token.key
            })
        except:
            return Response({
                'error':'Credenciales Enviadas Incorrectas'
            },status=status.HTTP_400_BAD_REQUEST)

class Login(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    
    def post(self,request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = authenticate(email = email,password=password)
            if user:
                if user.usuario_activo:
                    login_serializer = self.serializer_class(data=request.data)
                    if login_serializer.is_valid():
                        token, created = Token.objects.get_or_create(user=user)
                        user_data = UserSerializer(user).data
                        if created:
                            return Response({
                                    'token': token.key,
                                    'usuario': TokenSerializer(user).data,
                                    'message':'Inicio de Sesion Exitoso'
                                },
                                status=status.HTTP_200_OK
                            )
                        else:
                            all_sessions = Session.objects.filter(expire_date__gte = datetime.datetime.now())
                            if all_sessions.exists():
                                for session in all_sessions:
                                    session_data = session.get_decoded()
                                    if user_data['id'] == (session_data.get('_auth_user_id')):
                                        session.delete();
                            token.delete();
                            token = Token.objects.create(user=user)
                            usuario = TokenSerializer(user).data
                            datos = {}
                            datos=usuario['username'],usuario['email'],usuario['nombres'],usuario['apellidos'],Rol.objects.get(id=usuario['rol']).rol.lower(),usuario['jurisdiccion'],usuario['unidad_regional'],usuario['is_superuser']
                            print(datos)
                            return Response({
                                    'token': token.key,
                                    'usuario': datos,
                                    'mensaje':'inicio de Sesion Existoso'
                                },
                                status=status.HTTP_200_OK
                            )
                    return Response({'error':'Contrasenia o Email incorrectos'},status=status.HTTP_400_BAD_REQUEST)
                return Response({'error':'Este usuario no puede iniciar sesion.'},status=status.HTTP_401_UNAUTHORIZED)
            return Response({'error':'Contrasenia o Email incorrectos'},status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error':'Error de Busqueda de Usuario'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Logout(APIView):
    def post(self, request, *args, **kwargs):
        try:
            token = Token.objects.filter(key=request.POST['token']).first()
            print(request.POST['token'])
            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte = datetime.datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == (session_data.get('_auth_user_id')):
                            session.delete()
                
                token.delete()
                
                return Response({
                    'token_message': 'Token Eliminado',
                    'session_message': 'Sesiones de Usuario Eliminadas'
                }, status=status.HTTP_200_OK)    
            return Response({'error': 'No se ha encontrado un usuario con estas credenciales.'},
                            status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'No se ha encontrado token en la peticion'},
                            status=status.HTTP_409_CONFLICT)

