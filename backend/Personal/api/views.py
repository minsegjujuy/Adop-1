from ..models import Categoria, Funcionario, Personal, Jerarquia
from .serializer import (
    CategoriaSerializer,
    FuncionarioSerializer,
    PersonalSerializer,
    JerarquiaSerializer,
)
from BaseModel.api.views import DynamicModelViewSet
from Dependencia.models import Dependencia, UnidadRegional
from Persona.api.serializer import PersonaSerializer
from Persona.models import Persona
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import action


class PersonalViewSet(DynamicModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

    @action(detail=True, methods=["get"])
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

    @action(detail=True, methods=["get"])
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

    @action(detail=True, methods=["post"])
    def create(self, request, *args, **kwargs):
        serializer = PersonalSerializer(data=request)
        serializer.is_valid(raise_exception=True)
        personal = Personal()
        personal.legajo=serializer.validated_data["legajo"]
        personal.cuil=serializer.validated_data["fk_persona"]
        # personal.fk_tipo_funcion=serializer.validated_data['fk_tipo_funcion']
        personal.fk_jerarquia=serializer.validated_data["fk_jerarquia"]
        personal.fk_destino=serializer.validated_data["fk_destino"]
        personal.fk_jurisdiccion=serializer.validated_data["fk_jurisdiccion"]

        personal.new_save(usuario=request.user)

        return JsonResponse(
            {"msj": "Personal Creado Correctamente!!"}, status=status.HTTP_201_CREATED
        )


class JerarquiaViewSet(DynamicModelViewSet):
    queryset = Jerarquia.objects.all()
    serializer_class = JerarquiaSerializer


class CategoriaViewSet(DynamicModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class FuncionarioViewSet(DynamicModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
