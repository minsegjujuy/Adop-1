from ..models import Procedimiento, ProcedimientoPersona
from .serializer import ProcedimientoSerializer, ProcedimientoPersonaSerializer
from rest_framework import viewsets

class ProcedimientoViewSet(viewsets.ModelViewSet):
    queryset = Procedimiento.objects.all()    
    serializer_class = ProcedimientoSerializer
    
class ProcedimientoPersonaViewSet(viewsets.ModelViewSet):
    queryset = ProcedimientoPersona.objects.all()    
    serializer_class = ProcedimientoPersonaSerializer