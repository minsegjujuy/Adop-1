from ..models import Procedimiento, ProcedimientoPersona
from .serializer import ProcedimientoSerializer, ProcedimientoPersonaSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


class ProcedimientoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, TokenAuthentication)
    queryset = Procedimiento.objects.all()
    serializer_class = ProcedimientoSerializer


class ProcedimientoPersonaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, TokenAuthentication)
    queryset = ProcedimientoPersona.objects.all()
    serializer_class = ProcedimientoPersonaSerializer
