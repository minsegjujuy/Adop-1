import json
from Dependencia.models import Dependencia, UnidadRegional
from ..models import Personal, Jerarquia
from .serializer import PersonalSerializer,JerarquiaSerializer
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class PersonalViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Personal.objects.all()    
    serializer_class = PersonalSerializer
    
    def list(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()
        serializer = PersonalSerializer(self.queryset, many=True)
        respuesta = []
        for personal in serializer.data:
            data = {}
            data['legajo']=personal['legajo']
            data['cuil']=personal['cuil']
            data['fk_jerarquia'] = Jerarquia.objects.get(id=personal['fk_jerarquia']).nombre
            if personal['fk_destino']:
                data['fk_destino'] = Dependencia.objects.get(id=personal['fk_destino']).jurisdiccion
            else:
                data['fk_destino'] = "Sin definir"
            if personal['fk_jurisdiccion']:
                data['fk_jurisdiccion'] = UnidadRegional.objects.get(id=personal['fk_jurisdiccion']).unidad_regional
            else:
                data['fk_jurisdiccion'] = "Sin definir"
            respuesta.append(data)
        return JsonResponse(respuesta,safe=False,status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = PersonalSerializer(data=request)
        serializer.is_valid(raise_exception=True)
        Personal.objects.create(
            legajo=serializer.validated_data['legajo'],
            cuil=serializer.validated_data['cuil'],
            # fk_tipo_funcion=serializer.validated_data['fk_tipo_funcion'],
            fk_jerarquia=serializer.validated_data['fk_jerarquia'],
            fk_destino=serializer.validated_data['fk_destino'],
            fk_jurisdiccion=serializer.validated_data['fk_jurisdiccion']
        )
        return JsonResponse({'msj':'Personal Creado Correctamente!!'},status=status.HTTP_201_CREATED)

# class TipoFuncionViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (JWTAuthentication, TokenAuthentication)
#     queryset = TipoFuncion.objects.all()
#     serializer_class = TipoFuncionSerializer

#     @action(detail=True, methods=['get'])
#     def get(self, request, *args, **kwargs):
#         self.queryset=self.get_queryset()
#         serializer = TipoFuncionSerializer(self.queryset, many=True)
#         return JsonResponse(serializer,status=status.HTTP_200_OK)

#     @action(detail=True, methods=['post'])
#     def post(self, request, *args, **kwargs):
#         serializer = TipoFuncionSerializer(request)
#         serializer.is_valid(raise_exception=True)
#         TipoFuncion.objects.create(
#             tipo_funcion=serializer.validated_data['tipo_funcion']
#         )
#         return JsonResponse({'msj':'Elemento creado correctamente!!'},status=status.HTTP_201_CREATED)

class JerarquiaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, TokenAuthentication)
    queryset = Jerarquia.objects.all()
    serializer_class = JerarquiaSerializer

    @action(detail=True, methods=['get'])
    def get(self, *args, **kwargs):
        self.queryset=self.get_queryset()
        serializer = JerarquiaSerializer(self.queryset, many=True)
        return JsonResponse(serializer,status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def post(self, request, *args, **kwargs):
        serializer = JerarquiaSerializer(request)
        serializer.is_valid(raise_exception=True)
        Jerarquia.objects.create(
            nombre=serializer.validated_data['nombre'],
            nombre_largo=serializer.validated_data['nombre_largo'],
        )
        return JsonResponse({'msj':'Elemento creado correctamente!!'},status=status.HTTP_201_CREATED)
