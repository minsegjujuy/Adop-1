from ..models import Servicio, TipoRecurso, TipoServicio
from .serializer import TipoServicioSerializer, ServicioSerializer, RecursoSerializer
from rest_framework import viewsets, permissions

class TipoServicioViewSet(viewsets.ModelViewSet):
    queryset = TipoServicio.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ServicioSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoServicioSerializer

class RecursoViewSet(viewsets.ModelViewSet):
    queryset = TipoRecurso.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RecursoSerializer