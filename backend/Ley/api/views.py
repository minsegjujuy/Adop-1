from ..models import Ley, Articulo, Inciso
from .serializer import LeySerializer, ArticuloSerializer, IncisoSerializer
from BaseModel.api.views import DynamicModelViewSet


class LeyViewSet(DynamicModelViewSet):
    queryset = Ley.objects.all()
    serializer_class = LeySerializer


class ArticuloViewSet(DynamicModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer


class IncisoViewSet(DynamicModelViewSet):
    queryset = Inciso.objects.all()
    serializer_class = IncisoSerializer
