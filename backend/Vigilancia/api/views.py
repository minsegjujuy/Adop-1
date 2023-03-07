from ..models import Vigilancia, DiasVigilancia
from .serializer import VigilanciaSerializer, DiasVigilanciaSerializer
from rest_framework import viewsets, permissions

class VigilanciaViewSet(viewsets.ModelViewSet):
    queryset = Vigilancia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VigilanciaSerializer

class DiasVigilanciaViewSet(viewsets.ModelViewSet):
    queryset = DiasVigilancia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DiasVigilanciaSerializer