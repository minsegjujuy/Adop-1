from ..models import Dependencia, Inspectora, UnidadRegional, DependenciaOperativos
from .serializer import InspectoraSerializer, UnidadRegionalSerializer, DependenciaSerializer, DependenciaOperativosSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class InspectoraViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Inspectora.objects.all()    
    serializer_class = InspectoraSerializer

class UnidadRegionalViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = UnidadRegional.objects.all()    
    serializer_class = UnidadRegionalSerializer

class DependenciaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Dependencia.objects.all()    
    serializer_class = DependenciaSerializer

class DependenciasOperativosiewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = DependenciaOperativos.objects.all()    
    serializer_class = DependenciaOperativosSerializer