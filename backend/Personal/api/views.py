from ..models import Personal
from .serializer import PersonalSerializer
from rest_framework import viewsets, permissions

class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonalSerializer