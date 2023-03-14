from ..models import Personal
from .serializer import PersonalSerializer
from rest_framework import viewsets

class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()    
    serializer_class = PersonalSerializer