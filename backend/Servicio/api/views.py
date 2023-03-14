from ..models import Servicio, TipoRecurso, TipoServicio
from .serializer import TipoServicioSerializer, ServicioSerializer, RecursoSerializer
from rest_framework import viewsets

class TipoServicioViewSet(viewsets.ModelViewSet):
    queryset = TipoServicio.objects.all()
    serializer_class = ServicioSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = TipoServicioSerializer

class RecursoViewSet(viewsets.ModelViewSet):
    queryset = TipoRecurso.objects.all()    
    serializer_class = RecursoSerializer