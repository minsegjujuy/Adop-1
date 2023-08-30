from ..models import Servicio, TipoRecurso, TipoServicio
from .serializer import TipoServicioSerializer, ServicioSerializer, TipoRecursoSerializer
from BaseModel.api.views import DynamicModelViewSet


class TipoServicioViewSet(DynamicModelViewSet):
    queryset = TipoServicio.objects.all()
    serializer_class = TipoServicioSerializer


class ServicioViewSet(DynamicModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


class RecursoViewSet(DynamicModelViewSet):
    queryset = TipoRecurso.objects.all()
    serializer_class = TipoRecursoSerializer
