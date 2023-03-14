from ..models import Ley, Articulo, Inciso
from .serializer import LeySerializer, ArticuloSerializer, IncisoSerializer
from rest_framework import viewsets

class LeyViewSet(viewsets.ModelViewSet):
    queryset = Ley.objects.all()    
    serializer_class = LeySerializer

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()    
    serializer_class = ArticuloSerializer

class IncisoViewSet(viewsets.ModelViewSet):
    queryset = Inciso.objects.all()    
    serializer_class = IncisoSerializer