from ..models import Servicio, TipoRecurso, TipoServicio
from .serializer import TipoServicioSerializer, ServicioSerializer, TipoRecursoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


class TipoServicioViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, TokenAuthentication)
    queryset = TipoServicio.objects.all()
    serializer_class = TipoServicioSerializer


class ServicioViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, TokenAuthentication)
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


class RecursoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, TokenAuthentication)
    queryset = TipoRecurso.objects.all()
    serializer_class = TipoRecursoSerializer
