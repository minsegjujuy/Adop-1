from ..models import Procedimiento, ProcedimientoPersona
from .serializer import ProcedimientoSerializer, ProcedimientoPersonaSerializer
from BaseModel.api.views import DynamicModelViewSet


class ProcedimientoViewSet(DynamicModelViewSet):
    queryset = Procedimiento.objects.all()
    serializer_class = ProcedimientoSerializer


class ProcedimientoPersonaViewSet(DynamicModelViewSet):
    queryset = ProcedimientoPersona.objects.all()
    serializer_class = ProcedimientoPersonaSerializer
