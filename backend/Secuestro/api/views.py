from ..models import TipoSecuestro, Secuestro
from .serializer import SecuestroSerializer, TipoSecuestroSerializer
from rest_framework import viewsets

class TipoSecuestroViewSet(viewsets.ModelViewSet):
    queryset = TipoSecuestro.objects.all()    
    serializer_class = TipoSecuestroSerializer

class SecuestroViewSet(viewsets.ModelViewSet):
    queryset = Secuestro.objects.all()    
    serializer_class = SecuestroSerializer