from ..models import Ley, Articulo, Inciso
from .serializer import LeySerializer, ArticuloSerializer, IncisoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class LeyViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Ley.objects.all()    
    serializer_class = LeySerializer

class ArticuloViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Articulo.objects.all()    
    serializer_class = ArticuloSerializer

class IncisoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Inciso.objects.all()    
    serializer_class = IncisoSerializer