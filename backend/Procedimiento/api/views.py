from ..models import Procedimiento, ProcedimientoPersona
from .serializer import ProcedimientoSerializer, ProcedimientoPersonaSerializer
from rest_framework import viewsets, permissions

class ProcedimientoViewSet(viewsets.ModelViewSet):
    queryset = Procedimiento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProcedimientoSerializer
    
class ProcedimientoPersonaViewSet(viewsets.ModelViewSet):
    queryset = ProcedimientoPersona.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProcedimientoPersonaSerializer