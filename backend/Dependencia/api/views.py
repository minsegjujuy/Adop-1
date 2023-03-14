from ..models import Dependencia, Inspectora, UnidadRegional, DependenciaOperativos
from .serializer import InspectoraSerializer, UnidadRegionalSerializer, DependenciaSerializer, DependenciaOperativosSerializer
from rest_framework import viewsets

class InspectoraViewSet(viewsets.ModelViewSet):
    queryset = Inspectora.objects.all()    
    serializer_class = InspectoraSerializer

class UnidadRegionalViewSet(viewsets.ModelViewSet):
    queryset = Dependencia.objects.all()    
    serializer_class = DependenciaSerializer

class DependenciaViewSet(viewsets.ModelViewSet):
    queryset = UnidadRegional.objects.all()    
    serializer_class = UnidadRegionalSerializer

class DependenciasOperativosiewSet(viewsets.ModelViewSet):
    queryset = DependenciaOperativos.objects.all()    
    serializer_class = DependenciaOperativosSerializer