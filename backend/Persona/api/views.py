from ..models import Persona
from .serializer import PersonaSerializer
from rest_framework import viewsets, permissions

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonaSerializer