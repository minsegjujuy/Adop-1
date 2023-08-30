from .serializer import PersonaSerializer
from ..models import Persona
from BaseModel.api.views import DynamicModelViewSet


class PersonaViewSet(DynamicModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
