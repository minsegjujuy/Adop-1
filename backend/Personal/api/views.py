from Dependencia.models import Dependencia, UnidadRegional
from ..models import Personal, TipoFuncion, TipoEscalafon, TipoJerarquia, Jerarquia
from .serializer import PersonalSerializer,TipoFuncionSerializer,TipoEscalafonSerializer,TipoJerarquiaSerializer,JerarquiaSerializer
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
            data['id']=personal['id']
            data['legajo']=personal['legajo']
            data['cuil']=personal['cuil']
            data['domicilio']=personal['domicilio']
            data['genero']=personal['genero']
            data['nombre_apellido']=personal['nombre_apellido']
            data['fecha_nacimiento']=personal['fecha_nacimiento']
            data['estado_civil']=personal['estado_civil']
            data['nacionalidad']=personal['nacionalidad']
            data['fk_tipo_funcion'] = TipoFuncion.objects.get(id=personal['fk_tipo_funcion']).tipo_funcion
            data['fk_tipo_escalafon'] = TipoEscalafon.objects.get(id=personal['fk_tipo_escalafon']).tipo_escalafon
            data['fk_jerarquia'] = Jerarquia.objects.get(id=personal['fk_jerarquia']).nombre
            data['fk_destino'] = Dependencia.objects.get(id=personal['fk_destino']).jurisdiccion
            data['fk_jurisdiccion'] = UnidadRegional.objects.get(id=personal['fk_jurisdiccion']).unidad_regional
            respuesta.append(data)
        return JsonResponse(respuesta,status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = PersonalSerializer(data=request)
        serializer.is_valid(raise_exception=True)
        Personal.objects.create(
            legajo=serializer.validated_data['legajo'],
            cuil=serializer.validated_data['cuil'],
            fk_tipo_funcion=serializer.validated_data['fk_tipo_funcion'],
            fk_tipo_escalafon=serializer.validated_data['fk_tipo_escalafon'],
            fk_jerarquia=serializer.validated_data['fk_jerarquia'],
            fk_destino=serializer.validated_data['fk_destino'],
            fk_jurisdiccion=serializer.validated_data['fk_jurisdiccion'],
            domicilio=serializer.validated_data['domicilio'],
            genero=serializer.validated_data['genero'],
            nombre_apellido=serializer.validated_data['nombre_apellido'],
            fecha_nacimiento=serializer.validated_data['fecha_nacimiento'],
            estado_civil=serializer.validated_data['estado_civil'],
            nacionalidad=serializer.validated_data['nacionalidad']
        )
        return JsonResponse({'msj':'Personal Creado Correctamente!!'},status=status.HTTP_201_CREATED)

class TipoFuncionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, TokenAuthentication)
    queryset = TipoFuncion.objects.all()
    serializer_class = TipoFuncionSerializer

    @action(detail=True, methods=['get'])
    def get(self, request, *args, **kwargs):
        self.queryset=self.get_queryset()
        serializer = TipoFuncionSerializer(self.queryset, many=True)
        return JsonResponse(serializer,status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def post(self, request, *args, **kwargs):
        serializer = TipoFuncionSerializer(request)
        serializer.is_valid(raise_exception=True)
        TipoFuncion.objects.create(
            tipo_funcion=serializer.validated_data['tipo_funcion']
        )
        return JsonResponse({'msj':'Elemento creado correctamente!!'},status=status.HTTP_201_CREATED)

class TipoEscalafonViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, TokenAuthentication)
    queryset = TipoEscalafon.objects.all()
    serializer_class = TipoEscalafonSerializer

    @action(detail=True, methods=['get'])
    def get(self, request, *args, **kwargs):
        self.queryset=self.get_queryset()
        serializer = TipoEscalafonSerializer(self.queryset, many=True)
        return JsonResponse(serializer,status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def post(self, request, *args, **kwargs):
        serializer = TipoEscalafonSerializer(request)
        serializer.is_valid(raise_exception=True)
        TipoEscalafon.objects.create(
            tipo_escalafon=serializer.validated_data['tipo_escalafon']
        )
        return JsonResponse({'msj':'Elemento creado correctamente!!'},status=status.HTTP_201_CREATED)

class TipoJerarquiaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, TokenAuthentication)
    queryset = TipoJerarquia.objects.all()
    serializer_class = TipoJerarquiaSerializer

    @action(detail=True, methods=['get'])
    def get(self, request, *args, **kwargs):
        self.queryset=self.get_queryset()
        serializer = TipoJerarquiaSerializer(self.queryset, many=True)
        return JsonResponse(serializer,status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def post(self, request, *args, **kwargs):
        serializer = TipoJerarquiaSerializer(request)
        serializer.is_valid(raise_exception=True)
        TipoJerarquia.objects.create(
            tipo_jerarquia=serializer.validated_data['tipo_jerarquia']
        )
        return JsonResponse({'msj':'Elemento creado correctamente!!'},status=status.HTTP_201_CREATED)

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
            sumariante=serializer.validated_data['sumariante'],
            fk_tipo_jerarquia=serializer.validated_data['fk_tipo_jerarquia']
        )
        return JsonResponse({'msj':'Elemento creado correctamente!!'},status=status.HTTP_201_CREATED)
