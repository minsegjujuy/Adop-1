from ..models import Operativo, OperativoPersonal
from .serializer import OperativoSerializer, OperativoPersonalSerializer
from BaseModel.api.views import DynamicModelViewSet


class OperativoViewSet(DynamicModelViewSet):
    queryset = Operativo.objects.all()
    serializer_class = OperativoSerializer


class OperativoPersonalViewSet(DynamicModelViewSet):
    queryset = OperativoPersonal.objects.all()
    serializer_class = OperativoPersonalSerializer
