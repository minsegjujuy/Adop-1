from ..models import Ente
from .serializer import EnteSerializer
from BaseModel.api.views import DynamicModelViewSet


class EnteViewSet(DynamicModelViewSet):
    queryset = Ente.objects.all()
    serializer_class = EnteSerializer
