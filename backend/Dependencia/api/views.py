from ..models import Dependencia, Inspectora, UnidadRegional, DependenciaOperativos
from .serializer import InspectoraSerializer, UnidadRegionalSerializer, DependenciaSerializer, DependenciaOperativosSerializer
from rest_framework import viewsets, permissions

class InspectoraViewSet(viewsets.ModelViewSet):
    queryset = Inspectora.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InspectoraSerializer

class UnidadRegionalViewSet(viewsets.ModelViewSet):
    queryset = Dependencia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DependenciaSerializer

class DependenciaViewSet(viewsets.ModelViewSet):
    queryset = UnidadRegional.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UnidadRegionalSerializer

class DependenciasOperativosiewSet(viewsets.ModelViewSet):
    queryset = DependenciaOperativos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DependenciaOperativosSerializer