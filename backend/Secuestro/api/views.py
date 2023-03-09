from ..models import TipoSecuestro, Secuestro
from .serializer import SecuestroSerializer, TipoSecuestroSerializer
from rest_framework import viewsets, permissions

class TipoSecuestroViewSet(viewsets.ModelViewSet):
    queryset = TipoSecuestro.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TipoSecuestroSerializer

class SecuestroViewSet(viewsets.ModelViewSet):
    queryset = Secuestro.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SecuestroSerializer