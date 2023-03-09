from ..models import Ley, Articulo, Inciso
from .serializer import LeySerializer, ArticuloSerializer, IncisoSerializer
from rest_framework import viewsets, permissions

class LeyViewSet(viewsets.ModelViewSet):
    queryset = Ley.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LeySerializer

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ArticuloSerializer

class IncisoViewSet(viewsets.ModelViewSet):
    queryset = Inciso.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = IncisoSerializer