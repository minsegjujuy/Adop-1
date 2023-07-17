from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from Personal.api.serializer import PersonalSerializer
from .serializer import PersonaSerializer
from Persona.models import Persona
from Personal.models import Jerarquia, Personal
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class PersonaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Persona.objects.all()    
    serializer_class = PersonaSerializer
    
    # def retrieve(self, request, *args, **kwargs):
    #     legajo = kwargs['pk']
    #     personal = get_object_or_404(Personal, legajo=legajo)
    #     persona = get_object_or_404(Persona, cuil=personal.fk_persona.cuil)
    #     print(persona)
    #     respuesta = PersonaSerializer(persona).data['nombre_apellido']
    #     return JsonResponse(respuesta, safe=False, status=status.HTTP_200_OK)