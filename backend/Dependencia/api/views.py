from ..models import Dependencia, Inspectora, UnidadRegional, DependenciaOperativos
from .serializer import (
    InspectoraSerializer,
    UnidadRegionalSerializer,
    DependenciaSerializer,
    DependenciaOperativosSerializer,
)

from BaseModel.api.views import DynamicModelViewSet

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from django.http import JsonResponse


class InspectoraViewSet(DynamicModelViewSet):
    queryset = Inspectora.objects.all()
    serializer_class = InspectoraSerializer

    @action(detail=True, methods=["post"])
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        inspectora = Inspectora(
            nombre_inspectora=serializer.validated_data["nombre_inspectora"]
        )
        if request.user.is_authenticated:
            inspectora.new_save(usuario=request.user)
        else:
            inspectora.new_save()
        return JsonResponse(
            {"msj": "Inspectora creada correctamente"}, status=status.HTTP_201_CREATED
        )


class UnidadRegionalViewSet(DynamicModelViewSet):
    queryset = UnidadRegional.objects.all()
    serializer_class = UnidadRegionalSerializer

    @action(detail=True, methods=["get"])
    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.queryset = self.get_queryset().exclude(is_deleted=True)
            usuario = request.user
            serializer = UnidadRegionalSerializer(self.queryset, many=True)

            if usuario.rol.rol == "OPERADOR":
                datos = [
                    x
                    for x in serializer.data
                    if x["unidad_regional"] == usuario.unidad_regional.unidad_regional
                ]
            else:
                datos = serializer.data

            return JsonResponse(datos, status=status.HTTP_200_OK)
        else:
            return JsonResponse(
                {"error": "Carece de credenciales."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

    @action(detail=True, methods=["post"])
    def create(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()
        usuario = request.user
        if usuario.rol.rol == "ADMINISTRADOR":
            if (
                UnidadRegional.objects.filter(
                    unidad_regional=request.POST.get("unidad_regional")
                ).first()
                is None
            ):
                unidad_regional = UnidadRegional(
                    unidad_regional=request.POST.get("unidad_regional")
                )
                unidad_regional.new_save(usuario=request.user)
                return JsonResponse(
                    {"msj": "Unidad Regional creada con exito!!!"},
                    status=status.HTTP_201_CREATED,
                )
            else:
                respuesta = {"msj": "La Unidad Regional ingresada ya existe"}
                return JsonResponse(respuesta, status=status.HTTP_201_CREATED)
        else:
            respuesta = {
                "msj": "No tiene los permisos necesarios para realizar esta accion."
            }
            return JsonResponse(respuesta, status=status.HTTP_403_FORBIDDEN)


class DependenciaViewSet(DynamicModelViewSet):
    queryset = Dependencia.objects.all()
    serializer_class = DependenciaSerializer

    def list(self, request):
        self.queryset = self.get_queryset()
        usuario = request.user
        serializer = DependenciaSerializer(self.queryset, many=True)
        if not usuario.is_anonymous and usuario.rol.rol == "OPERADOR":
            datos = [
                x
                for x in serializer.data
                if x["fk_unidad_regional"] == usuario.unidad_regional.id
            ]
        else:
            try:
                ur = int(request.GET["uurr"])
                if ur != 0:
                    datos = [
                        x for x in serializer.data if x["fk_unidad_regional"] == ur
                    ]
                else:
                    datos = serializer.data
            except:
                datos = serializer.data

        respuesta = []

        for uurr in datos:
            data = {}
            data["id"] = uurr["id"]
            data["jurisdiccion"] = uurr["jurisdiccion"]
            respuesta.append(data)
        return Response(respuesta)


class DependenciasOperativosiewSet(DynamicModelViewSet):
    queryset = DependenciaOperativos.objects.all()
    serializer_class = DependenciaOperativosSerializer
