from ..models import Operativo, OperativoPersonal
from .serializer import OperativoSerializer, OperativoPersonalSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


class OperativoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, TokenAuthentication)
    queryset = Operativo.objects.all()
    serializer_class = OperativoSerializer


class OperativoPersonalViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, TokenAuthentication)
    queryset = OperativoPersonal.objects.all()
    serializer_class = OperativoPersonalSerializer
