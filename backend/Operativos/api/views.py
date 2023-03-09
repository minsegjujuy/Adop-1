from ..models import Operativo, OperativoPersonal
from .serializer import OperativoSerializer, OperativoPersonalSerializer
from rest_framework import viewsets, permissions

class OperativoViewSet(viewsets.ModelViewSet):
    queryset = Operativo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OperativoSerializer

class OperativoPersonalViewSet(viewsets.ModelViewSet):
    queryset = OperativoPersonal.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OperativoPersonalSerializer