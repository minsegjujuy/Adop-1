from Dependencia.models import Dependencia, UnidadRegional
from Persona.api.serializer import PersonaSerializer
from Persona.models import Persona
from ..models import Categoria, Funcionario, Personal, Jerarquia
from .serializer import (
    CategoriaSerializer,
    FuncionarioSerializer,
    PersonalSerializer,
    JerarquiaSerializer,
)
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


class PersonalViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, TokenAuthentication)
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

    def list(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()
        serializer = PersonalSerializer(self.queryset, many=True)
        respuesta = []
        for personal in serializer.data:
            data = {}
            data["legajo"] = personal["legajo"]
            data["cuil"] = personal["fk_persona"]
            data["nombre_apellido"] = PersonaSerializer(
                Persona.objects.get(cuil=personal["fk_persona"])
            ).data["nombre_apellido"]
            data["fk_jerarquia"] = Jerarquia.objects.get(
                id=personal["fk_jerarquia"]
            ).nombre
            if personal["fk_destino"]:
                data["fk_destino"] = Dependencia.objects.get(
                    id=personal["fk_destino"]
                ).jurisdiccion
            else:
                data["fk_destino"] = "Sin definir"
            if personal["fk_jurisdiccion"]:
                data["fk_jurisdiccion"] = UnidadRegional.objects.get(
                    id=personal["fk_jurisdiccion"]
                ).unidad_regional
            else:
                data["fk_jurisdiccion"] = "Sin definir"
            respuesta.append(data)
        return JsonResponse(respuesta, safe=False, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        legajo = kwargs["pk"]
        personal = PersonalSerializer(Personal.objects.get(legajo=legajo)).data
        persona = PersonaSerializer(
            Persona.objects.get(cuil=personal["fk_persona"])
        ).data

        data = {}
        data["legajo"] = personal["legajo"]
        data["cuil"] = persona["cuil"]
        data["dni"] = persona["dni"]
        data["nombre_apellido"] = persona["nombre_apellido"]
        data["fecha_nacimiento"] = persona["fecha_nacimiento"]
        data["jerarquia"] = Jerarquia.objects.get(
            id=personal["fk_jerarquia"]
        ).nombre_largo
        data["dependencia"] = personal["fk_destino"]
        data["jurisdiccion"] = personal["fk_jurisdiccion"]
        return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = PersonalSerializer(data=request)
        serializer.is_valid(raise_exception=True)
        Personal.objects.create(
            legajo=serializer.validated_data["legajo"],
            cuil=serializer.validated_data["fk_persona"],
            # fk_tipo_funcion=serializer.validated_data['fk_tipo_funcion'],
            fk_jerarquia=serializer.validated_data["fk_jerarquia"],
            fk_destino=serializer.validated_data["fk_destino"],
            fk_jurisdiccion=serializer.validated_data["fk_jurisdiccion"],
        )
        return JsonResponse(
            {"msj": "Personal Creado Correctamente!!"}, status=status.HTTP_201_CREATED
        )


class JerarquiaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, TokenAuthentication)
    serializer_class = JerarquiaSerializer

    def get_queryset(self):
        queryset = Jerarquia.objects.filter(...)
        return queryset

    @action(detail=True, methods=["get"])
    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = JerarquiaSerializer(queryset, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def post(self, request, *args, **kwargs):
        serializer = JerarquiaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(
            {"msj": "Elemento creado correctamente!!"}, status=status.HTTP_201_CREATED
        )


class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, TokenAuthentication)
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, TokenAuthentication)
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
