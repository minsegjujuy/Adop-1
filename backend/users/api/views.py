from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.sessions.models import Session

from users.models import Usuario
from users.api.serializers import UserSerializer, TokenSerializer

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

class UserViewSet(Authentication,viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,IsAuthenticated)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Usuario.objects.all()    
    serializer_class = UserSerializer

class UserView (APIView):
    permission_classes = (IsAdminUser,IsAuthenticated)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    
class RefreshToken(APIView):
    def get(slef,request,*args, **kwargs):
        username = request.GET.get('username')
        print(username)
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
        email = request.data.get('email', '')
        password = request.data.get('password', '')
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
                            return Response({
                                    'token': token.key,
                                    'usuario': TokenSerializer(user).data,
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

