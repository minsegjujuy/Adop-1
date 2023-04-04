from ..models import Motivo,Vigilancia, DiasVigilancia
from Dependencia.models import Dependencia, UnidadRegional
from Servicio.models import Servicio

from Dependencia.api.serializer import UnidadRegionalSerializer
from .serializer import VigilanciaSerializer, DiasVigilanciaSerializer, MotivoVigilanciaSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class MotivoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Motivo.objects.all()    
    serializer_class = MotivoVigilanciaSerializer

class VigilanciaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Vigilancia.objects.all()    
    serializer_class = VigilanciaSerializer
    
    def list(self, request):
        usuario = request.user
        serializer = VigilanciaSerializer(self.queryset, many=True)
        # print(serializer)
        if usuario.rol == 'operador':
            for vigilancia in serializer.data:
                if vigilancia.fk_jurisdiccion != usuario.jurisdiccion:
                    serializer.data.pop(vigilancia, None)
        # print(serializer)
        resuesta = []
        for vigilancia in serializer.data:
            data = {}
            data['id']=vigilancia['id']
            data['jurisdiccion']= Dependencia.objects.get(id=vigilancia['fk_jurisdiccion']).jurisdiccion
            data['motivo']= Motivo.objects.get(id=vigilancia['fk_motivo']).motivo
            try:
                data['servicio']=Servicio.objects.get(id=vigilancia['fk_servicio']).servicio
            except:
                data['servicio']=None
            data['regional'] = UnidadRegionalSerializer(Dependencia.objects.get(id=vigilancia['fk_jurisdiccion']).fk_unidad_regional).data['unidad_regional']
            data['objetivo']= vigilancia['objetivo']
            data['cant_dias']= vigilancia['cant_dias']
            data['fecha_inicio']= vigilancia['fecha_inicio']
            data['fecha_fin']= vigilancia['fecha_fin']
            data['destino']= vigilancia['destino']
            data['longitud']= vigilancia['longitud']
            data['latitud']= vigilancia['latitud']
            
            resuesta.append(data)
        
        return Response(resuesta)

    def retrieve(self, request, pk=None):
        try:
            queryset = Vigilancia.objects.get(pk=pk)
        except Vigilancia.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer_data = VigilanciaSerializer(queryset).data
        
        data = {}
       
        data['id']=serializer_data['id']
        data['jurisdiccion']= Dependencia.objects.get(id=serializer_data['fk_jurisdiccion']).jurisdiccion
        data['motivo']= Motivo.objects.get(id=serializer_data['fk_motivo']).motivo
        try:
            data['servicio']=Servicio.objects.get(id=serializer_data['fk_servicio']).servicio
        except:
            data['servicio']=None
        data['regional'] = UnidadRegionalSerializer(Dependencia.objects.get(id=serializer_data['fk_jurisdiccion']).fk_unidad_regional).data['unidad_regional']
        data['objetivo']= serializer_data['objetivo']
        data['cant_dias']= serializer_data['cant_dias']
        data['fecha_inicio']= serializer_data['fecha_inicio']
        data['fecha_fin']= serializer_data['fecha_fin']
        data['destino']= serializer_data['destino']
        data['longitud']= serializer_data['longitud']
        data['latitud']= serializer_data['latitud']
        
        return Response(data)
    
    def create(self, request, *args, **kwargs):
        serializer = VigilanciaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        fk_jurisdiccion = serializer.validated_data.get('fk_jurisdiccion')
        fk_motivo = serializer.validated_data.get('fk_motivo')
        fk_tipo_servicio = serializer.validated_data.get('fk_tipo_servicio')
        fk_tipo_recurso = serializer.validated_data.get('fk_tipo_recurso')
        regional = serializer.validated_data.get('regional')
        objetivo = serializer.validated_data.get('objetivo')
        cant_dias = serializer.validated_data.get('cant_dias')
        fecha_inicio = serializer.validated_data.get('fecha_inicio')
        fecha_fin = serializer.validated_data.get('fecha_fin')
        destino = serializer.validated_data.get('destino')
        longitud = serializer.validated_data.get('longitud')
        latitud = serializer.validated_data.get('latitud')
        
        Vigilancia.objects.create(
            fk_jurisdiccion = fk_jurisdiccion,
            fk_motivo = fk_motivo,
            fk_tipo_servicio = fk_tipo_servicio,
            fk_tipo_recurso = fk_tipo_recurso,
            regional = regional,
            objetivo = objetivo,
            cant_dias = cant_dias,
            fecha_inicio = fecha_inicio,
            fecha_fin = fecha_fin,
            destino = destino,
            longitud = longitud,
            latitud = latitud
        )
        
        respuesta = {'msj':'Vigilancia creada exitosamente!'}
        return JsonResponse(respuesta, safe=False,status = status.HTTP_201_CREATED)
    
class DiasVigilanciaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = DiasVigilancia.objects.all()    
    serializer_class = DiasVigilanciaSerializer
    
    # def list(self, request):
    #     serializer = DiasVigilanciaSerializer(self.queryset, many=True)
    #     resuesta = []
    #     for dvig in serializer.data:
    #         data = {}
    #         data['id']=dvig['id']
    #         data['fk_vigilancia']=dvig['fk_vigilancia']
    #         data['fk_personal']=dvig['fk_personal']
    #         data['dia']=dvig['dia']
    #         data['hora_inicio']=dvig['hora_inicio']
    #         data['hora_fin']=dvig['hora_fin']
    #         data['turno']=dvig['turno']
    #         data['dia_completo']=dvig['dia_completo']
            
    #         resuesta.append(data)
        
    #     return Response(resuesta)