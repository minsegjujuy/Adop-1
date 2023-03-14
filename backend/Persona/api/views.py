from ..models import Persona
from .serializer import PersonaSerializer
from rest_framework import viewsets

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()    
    serializer_class = PersonaSerializer