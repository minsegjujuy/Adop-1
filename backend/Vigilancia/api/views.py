from ..models import Vigilancia, DiasVigilancia
from .serializer import VigilanciaSerializer, DiasVigilanciaSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class VigilanciaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Vigilancia.objects.all()    
    serializer_class = VigilanciaSerializer
    
class DiasVigilanciaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = DiasVigilancia.objects.all()    
    serializer_class = DiasVigilanciaSerializer