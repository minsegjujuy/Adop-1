from ..models import TipoSecuestro, Secuestro
from .serializer import SecuestroSerializer, TipoSecuestroSerializer
from BaseModel.api.views import DynamicModelViewSet


class TipoSecuestroViewSet(DynamicModelViewSet):
    queryset = TipoSecuestro.objects.all()
    serializer_class = TipoSecuestroSerializer


class SecuestroViewSet(DynamicModelViewSet):
    queryset = Secuestro.objects.all()
    serializer_class = SecuestroSerializer
