from ..models import Vigilancia, DiasVigilancia
from .serializer import VigilanciaSerializer, DiasVigilanciaSerializer
from rest_framework import viewsets

class VigilanciaViewSet(viewsets.ModelViewSet):
    queryset = Vigilancia.objects.all()    
    serializer_class = VigilanciaSerializer

class DiasVigilanciaViewSet(viewsets.ModelViewSet):
    queryset = DiasVigilancia.objects.all()    
    serializer_class = DiasVigilanciaSerializer