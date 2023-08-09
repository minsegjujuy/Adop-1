from ..models import TipoSecuestro, Secuestro
from .serializer import SecuestroSerializer, TipoSecuestroSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


class TipoSecuestroViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, TokenAuthentication)
    queryset = TipoSecuestro.objects.all()
    serializer_class = TipoSecuestroSerializer


class SecuestroViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, TokenAuthentication)
    queryset = Secuestro.objects.all()
    serializer_class = SecuestroSerializer
