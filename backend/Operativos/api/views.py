from ..models import Operativo, OperativoPersonal
from .serializer import OperativoSerializer, OperativoPersonalSerializer
from rest_framework import viewsets

class OperativoViewSet(viewsets.ModelViewSet):
    queryset = Operativo.objects.all()    
    serializer_class = OperativoSerializer

class OperativoPersonalViewSet(viewsets.ModelViewSet):
    queryset = OperativoPersonal.objects.all()    
    serializer_class = OperativoPersonalSerializer