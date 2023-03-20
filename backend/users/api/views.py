from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.sessions.models import Session

from users.models import Usuario
from users.api.serializers import UserSerializer, TokenSerializer

from rest_framework import status, viewsets
from rest_framework.views import APIView
# from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from rest_framework.authtoken.models import Token

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

import datetime

from .permisos import (
    PermisoAdministrador,
    PermisoOperador,
    PermisoFarmaceutico,
)

from ..authentication_mixins import Authentication

# class UserApiViewSet(ModelViewSet):
#     permission_classes = [IsAdminUser]
#     serializer_class = UserSerializer
#     queryset = Usuario.objects.all()

#     def create(self, request, *args, **kwargs):
#         request.data['password'] = make_password(request.data['password'])
#         return super().create(request, *args, **kwargs)

#     def partial_update(self, request, *args, **kwargs):
#         password = request.data['password']

#         if password:
#             request.data['password'] = make_password(password)
#         else:
#             request.data['password'] = request.user.password
#         return super().update(request, *args, **kwargs)

class UserViewSet(viewsets.ModelViewSet):
# class UserViewSet(Authentication,viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Usuario.objects.all()    
    serializer_class = UserSerializer

class UserView (APIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    

class Login(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    
    def post(self,request, *args, **kwargs):
        email = request.data.get('email', '')
        password = request.data.get('password', '')
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

