from ..models import Motivo, Vigilancia, TurnosVigilancia, PersonalVigilancia
from Personal.models import Personal
from Dependencia.models import Dependencia
from Servicio.models import TipoServicio, TipoRecurso

from Dependencia.api.serializer import UnidadRegionalSerializer
from .serializer import VigilanciaSerializer, VigilanciaSerializerView, TurnosVigilanciaSerializerView, TurnosVigilanciaSerializer, MotivoVigilanciaSerializer, PersonalVigilanciaSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from datetime import datetime, date, timedelta
import calendar
import locale
from django.http import JsonResponse
locale.setlocale(locale.LC_TIME, "es_ES")

class MotivoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Motivo.objects.all()    
    serializer_class = MotivoVigilanciaSerializer

class VigilanciaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Vigilancia.objects.all()
    serializer_class = VigilanciaSerializerView
    
    def list(self, request, *args, **kwargs):
        usuario = request.user
        inactivo = request.GET.get('inactivo')
        # print(inactivo)
        self.queryset = self.get_queryset()
        serializer = VigilanciaSerializerView(self.queryset, many=True)
        # print(serializer.data)
        if usuario.rol.rol == 'OPERADOR':
            if inactivo:
                datos = [x for x in serializer.data if x['fk_unidad_regional']==usuario.unidad_regional.id and datetime.now()<x['fecha_fin']]
            else:
                datos = [x for x in serializer.data if x['fk_unidad_regional']==usuario.unidad_regional.id]
        else:
            datos = serializer.data

        resuesta = []
        for vigilancia in datos:
            data = {}
            data['id']=vigilancia['id']
            data['jurisdiccion']= Dependencia.objects.get(id=vigilancia['fk_jurisdiccion']).jurisdiccion
            data['motivo']= Motivo.objects.get(id=vigilancia['fk_motivo']).motivo
            try:
                data['servicio']=TipoServicio.objects.get(id=vigilancia['fk_tipo_servicio']).tipo_servicio
            except:
                data['servicio']=None
            data['fk_unidad_regional'] = UnidadRegionalSerializer(Dependencia.objects.get(id=vigilancia['fk_jurisdiccion']).fk_unidad_regional).data['unidad_regional']
            data['objetivo']= vigilancia['objetivo']
            data['cant_dias']= vigilancia['cant_dias']
            data['fecha_inicio']= vigilancia['fecha_inicio']
            if vigilancia['fecha_fin']:
                data['fecha_fin'] = vigilancia['fecha_fin']
            else:
                data['fecha_fin'] = "Indefinido"
            data['turno_asignado'] = vigilancia['turno_asignado']
            data['destino']= vigilancia['destino']
            data['longitud']= vigilancia['longitud']
            data['latitud']= vigilancia['latitud']
            
            resuesta.append(data)
        
        return Response(resuesta)

    def retrieve(self, request, pk=None):
        self.queryset = self.get_queryset()
        try:
            queryset = Vigilancia.objects.get(pk=pk)
        except Vigilancia.DoesNotExist:
            return JsonResponse({'msj':'No se encontro la Vigilancia'},status=status.HTTP_404_NOT_FOUND)

        serializer_data = VigilanciaSerializerView(queryset).data
        
        data = {}
       
        data['id']=serializer_data['id']
        data['jurisdiccion']= Dependencia.objects.get(id=serializer_data['fk_jurisdiccion']).jurisdiccion
        data['motivo']= Motivo.objects.get(id=serializer_data['fk_motivo']).motivo
        try:
            data['servicio']=TipoServicio.objects.get(id=serializer_data['fk_tipo_servicio']).tipo_servicio
        except:
            data['servicio']=None
        data['recurso'] = TipoRecurso.objects.get(id=serializer_data['fk_tipo_recurso']).tipo_recurso
        data['regional'] = UnidadRegionalSerializer(Dependencia.objects.get(id=serializer_data['fk_jurisdiccion']).fk_unidad_regional).data['unidad_regional']
        data['objetivo']= serializer_data['objetivo']
        data['cant_dias']= serializer_data['cant_dias']
        data['fecha_inicio']= serializer_data['fecha_inicio']
        data['fecha_fin']= serializer_data['fecha_fin']
        data['turno_asignado'] = serializer_data['turno_asignado']
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
        fk_unidad_regional = serializer.validated_data.get('fk_unidad_regional')
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
            fk_unidad_regional = fk_unidad_regional,
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
    
    def destroy(self, request, pk=None):
        try:
            vigilancia = Vigilancia.objects.get(pk=pk)
            vigilancia.delete()
            return JsonResponse({'msj':'Vigilancia Eliminada Correctamente!!!'},status=status.HTTP_200_OK)
        except Vigilancia.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class TurnosVigilanciaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = TurnosVigilancia.objects.all()
    serializer_class = TurnosVigilanciaSerializerView

    def seleccionar_fechas(self, fecha_inicio, fecha_fin, diario, dias_semana):
        fechas = []
        fechas_seleccionadas = []
        fecha_actual = fecha_inicio
        fecha_limite = fecha_fin
        
        if fecha_limite is None:
            fecha_limite = fecha_actual + timedelta(days=7)

        while fecha_actual <= fecha_limite:
            fechas.append(fecha_actual)
            if diario == False:
                fechas = [x for x in fechas if x.strftime('%A') in dias_semana]
            fecha_actual += timedelta(days=1)
        
        for fecha in fechas:
            fechas_seleccionadas.append(str(fecha)[:10])

        return fechas_seleccionadas

    def create(self,request, *args, **kwargs):
        serializer = TurnosVigilanciaSerializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        vigilancia = serializer.validated_data['fk_vigilancia'].id
        
        fechas = self.seleccionar_fechas(Vigilancia.objects.get(id=vigilancia).fecha_inicio,Vigilancia.objects.get(id=vigilancia).fecha_fin,serializer.validated_data['diario'],serializer.validated_data['turno'])

        # print(datetime.now().time().isoformat())
        # print(datetime.now().time().hour)
        # print(datetime.now().time().minute)

        # print(hora_inicio.hour)
        # print(hora_fin.hour)

        if serializer.validated_data['dia_completo']:
            serializer.validated_data['hora_inicio'] = None
            serializer.validated_data['hora_fin'] = None
            serializer.validated_data['duracion'] = 24
        else:
            serializer.validated_data['hora_fin'] = (
                datetime.combine(
                        date.today(),
                        serializer.validated_data['hora_inicio']
                    ) +
                    timedelta(
                        hours=serializer.validated_data['duracion']
                    )
                ).time()
        try:
            TurnosVigilancia.objects.create(
                fk_vigilancia = serializer.validated_data['fk_vigilancia'],
                turno = fechas,
                hora_inicio = serializer.validated_data['hora_inicio'],
                hora_fin = serializer.validated_data['hora_fin'],
                duracion = serializer.validated_data['duracion'],
                diario = serializer.validated_data['diario'],
                dia_completo = serializer.validated_data['dia_completo']
            )
            up_vigilancia = get_object_or_404(Vigilancia, pk=vigilancia)
            up_vigilancia.turno_asignado = True
            up_vigilancia.cant_dias = len(fechas)
            up_vigilancia.save()

            respuesta = {"msj":"Turnos Asignados Correctamente!!!"}
            return JsonResponse(respuesta, safe=False,status = status.HTTP_201_CREATED)
        except ValueError:
            respuesta = {"error":"Error al crear los Turnos"}
            return JsonResponse(respuesta, safe=False, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class PersonalVigilanciaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = PersonalVigilancia.objects.all()    
    serializer_class = PersonalVigilanciaSerializer
    
    def list(self, *args,  **kwargs):
        self.queryset = self.get_queryset()
        try:
            turno = TurnosVigilancia.objects.get(fk_vigilancia=kwargs['vigilancia_id'])
            serializer = TurnosVigilanciaSerializerView(turno)
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        except:
            return JsonResponse({'msj':'La vigilancia no tiene ningun turno asignada'},status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request, *args, **kwargs):
        fk_vigilancia = kwargs['vigilancia_id']
        
        turno = TurnosVigilancia.objects.get(fk_vigilancia=fk_vigilancia)
        serializer = TurnosVigilanciaSerializerView(turno)
        
        fk_turnoVigilancia = serializer.data['id']
        
        datos_agregar = []
        for t in request.data['turnos']:
            fecha=datetime.strptime(t[0],"%Y-%m-%d").date()
            for f in t[1]:
                personal_vigilancia = {
                    "fk_personal":f['fk_personal'],
                    "fk_turnoVigilancia": fk_turnoVigilancia,
                    "fecha":fecha,
                    "hora_inicio":f['hora_inicio'],
                    "hora_fin":f['hora_fin']
                }
                if personal_vigilancia['fk_personal']:
                    personal_vigilancia['asignado'] = True
                else:
                    personal_vigilancia['asignado'] = False
                datos_agregar.append(personal_vigilancia)
        
        for dato in datos_agregar:
            serializer = PersonalVigilanciaSerializer(data = dato)
            serializer.is_valid(raise_exception=True)
            PersonalVigilancia.objects.create(
                fk_personal = serializer.validated_data['fk_personal'],
                fk_turnoVigilancia = serializer.validated_data['fk_turnoVigilancia'],
                fecha = serializer.validated_data['fecha'],
                hora_inicio = serializer.validated_data['hora_inicio'],
                hora_fin = serializer.validated_data['hora_fin'],
                asignado = serializer.validated_data['asignado']
            )
        return JsonResponse({"msj":"Personal Asignado Correctamente"},status=status.HTTP_201_CREATED)
        # return JsonResponse({"cant_datos":len(datos_agregar),"datos":datos_agregar})
        
    def update(self, request, pk=None):
        personalVigilancia = self.get_object(pk)
        serializer = PersonalVigilancia(data = personalVigilancia)
        if serializer.data['fk_personal']:
            if request.data['fk_personal']!=serializer.data['fk_personal'].id:
                if request.data['fk_personal']:
                    serializer.data['fk_personal']=Personal.objects.get(id=request.data['fk_personal'])
                else:
                    serializer.data['fk_personal']=None
                    serializer.data['asignado']=False
                serializer.save()
        return JsonResponse({"msj":'Turno Modificado correctamente!!'},status=status.HTTP_200_OK)
