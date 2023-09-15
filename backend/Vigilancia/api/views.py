from ..models import (
    Motivo,
    Vigilancia,
    TurnosVigilancia,
    PersonalVigilancia,
    RecursosVigilancia,
)
from .serializer import (
    VigilanciaSerializer,
    VigilanciaSerializerView,
    RecursosVigilanciaSerializer,
    TurnosVigilanciaSerializer,
    MotivoVigilanciaSerializer,
    PersonalVigilanciaSerializer,
)

from Personal.models import Personal
from Persona.models import Persona
from Dependencia.models import Dependencia
from Servicio.models import TipoServicio, TipoRecurso
from Personal.models import Funcionario
from Ente.models import Ente

from Servicio.api.serializer import TipoRecursoSerializer
from Dependencia.api.serializer import UnidadRegionalSerializer
from Personal.api.serializer import PersonalSerializer, FuncionarioSerializer
from Ente.api.serializer import EnteSerializer
from BaseModel.api.views import DynamicModelViewSet

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.decorators import action

from django.http import JsonResponse
from datetime import datetime, date, timedelta
import locale

locale.setlocale(locale.LC_TIME, "es_ES")


class MotivoViewSet(DynamicModelViewSet):
    queryset = Motivo.objects.all()
    serializer_class = MotivoVigilanciaSerializer


class VigilanciaViewSet(DynamicModelViewSet):
    queryset = Vigilancia.objects.all()
    serializer_class = VigilanciaSerializerView

    @action(detail=True, methods=['GET'])
    def list(self, request, *args, **kwargs):
        usuario = request.user
        # inactivo = request.GET.get("inactivo")
        # print(inactivo)
        self.queryset = self.get_queryset()
        serializer = VigilanciaSerializerView(self.queryset, many=True)
        if usuario.rol.rol == "OPERADOR":
            # if inactivo:
            #     datos = [x for x in serializer.data if x["fk_unidad_regional"] == usuario.unidad_regional.id and datetime.now() < x["fecha_fin"]]
            # else:
            datos = [x for x in serializer.data if x["fk_unidad_regional"] == usuario.unidad_regional.id]
        else:
            datos = serializer.data

        resuesta = []
        for vigilancia in datos:
            data = {}
            data["id"] = vigilancia["id"]
            data["jurisdiccion"] = Dependencia.objects.get(id=vigilancia["fk_jurisdiccion"]).jurisdiccion
            data["motivo"] = Motivo.objects.get(id=vigilancia["fk_motivo"]).motivo
            try:
                data["servicio"] = TipoServicio.objects.get(id=vigilancia["fk_tipo_servicio"]).tipo_servicio
            except:
                data["servicio"] = None
            data["fk_unidad_regional"] = UnidadRegionalSerializer(Dependencia.objects.get(id=vigilancia["fk_jurisdiccion"]).fk_unidad_regional).data["unidad_regional"]
            if vigilancia["fk_ente"]:
                data["fk_ente"] = EnteSerializer(Ente.objects.get(id=vigilancia["fk_ente"])).data
            if vigilancia["fk_funcionario"]:
                data["fk_funcionario"] = FuncionarioSerializer(Funcionario.objects.get(id=vigilancia["fk_funcionario"])).data
            data["objetivo"] = vigilancia["objetivo"]
            data["cant_dias"] = vigilancia["cant_dias"]
            data["fecha_inicio"] = vigilancia["fecha_inicio"]
            if vigilancia["fecha_fin"]:
                data["fecha_fin"] = vigilancia["fecha_fin"]
            else:
                data["fecha_fin"] = "Indefinido"
            data["turno_asignado"] = vigilancia["turno_asignado"]
            data["destino"] = vigilancia["destino"]
            data["longitud"] = vigilancia["longitud"]
            data["latitud"] = vigilancia["latitud"]

            resuesta.append(data)

        return Response(resuesta)

    @action(detail=True, methods=['GET'])
    def retrieve(self, request, pk=None):
        self.queryset = self.get_queryset()
        try:
            queryset = Vigilancia.objects.get(pk=pk)
        except Vigilancia.DoesNotExist:
            return JsonResponse(
                {"msj": "No se encontro la Vigilancia"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer_data = VigilanciaSerializerView(queryset).data

        data = {}

        data["id"] = serializer_data["id"]
        data["jurisdiccion"] = Dependencia.objects.get(id=serializer_data["fk_jurisdiccion"]).jurisdiccion
        data["motivo"] = Motivo.objects.get(id=serializer_data["fk_motivo"]).motivo

        try:
            data["servicio"] = TipoServicio.objects.get(id=serializer_data["fk_tipo_servicio"]).tipo_servicio
        except:
            data["servicio"] = None

        try:
            data["ente"] = Ente.objects.get(id=serializer_data["fk_ente"]).nombre
        except:
            data["ente"] = None

        try:
            funcionario = Funcionario.objects.get(id=serializer_data["fk_funcionario"])
            data["funcionario"] = f"{funcionario.fk_persona.cuil} - {funcionario.fk_persona.nombre_apellido} - {funcionario.fk_categoria.fk_categoria.nombre} {funcionario.fk_categoria.fk_categoria.nombre}"
        except:
            data["funcionario"] = None

        # data['recurso'] = TipoRecurso.objects.get(id=serializer_data['fk_tipo_recurso']).tipo_recurso
        # Si viene una de las fechas de la vigilancia se obtienen los recursos que se uitilizaron ese dia
        if request.GET.get("fecha"):
            data["recursos"] = []
            for recurso in RecursosVigilancia.objects.filter(fk_vigilancia=pk, fecha=datetime.strptime(request.GET.get("fecha"), "%Y-%m-%d").date()):
                recurso = RecursosVigilanciaSerializer(recurso).data
                tipo_rec = TipoRecursoSerializer(TipoRecurso.objects.get(id=recurso['fk_tipo_recurso'])).data
                data["recursos"].append({tipo_rec["id"]: [tipo_rec["tipo_recurso"], recurso["cantidad"]]})

        data["regional"] = UnidadRegionalSerializer(Dependencia.objects.get(id=serializer_data["fk_jurisdiccion"]).fk_unidad_regional).data["unidad_regional"]
        data["objetivo"] = serializer_data["objetivo"]
        data["cant_dias"] = serializer_data["cant_dias"]
        data["fecha_inicio"] = serializer_data["fecha_inicio"]
        data["fecha_fin"] = serializer_data["fecha_fin"]
        data["turno_asignado"] = serializer_data["turno_asignado"]
        data["destino"] = serializer_data["destino"]
        data["longitud"] = serializer_data["longitud"]
        data["latitud"] = serializer_data["latitud"]

        return Response(data)

    @action(detail=True, methods=['POST'])
    def create(self, request, *args, **kwargs):
        serializer = VigilanciaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        vigilancia = Vigilancia(**serializer.validated_data)
        
        # fk_tipo_recurso = serializer.validated_data.get("fk_tipo_recurso")
        
        vigilancia.new_save(usuario=request.user)

        respuesta = {"msj": "Vigilancia creada exitosamente!"}
        return JsonResponse(respuesta, safe=False, status=status.HTTP_201_CREATED)


class RecursosVigilanciaViewSet(DynamicModelViewSet):
    queryset = RecursosVigilancia.objects.all()
    serializer_class = RecursosVigilanciaSerializer
    # la fecha que se tiene que enviar en la tea es la fecha de la vigilancia
    
    @action(detail=True, methods=['post'])
    def create(self, request, *args, **kwargs):
        try:
            vigilancia = Vigilancia.objects.get(id=kwargs['pk'])
            serializer = RecursosVigilanciaSerializer(request.data).data
            serializer['fk_vigilancia'] = vigilancia
            
            recurso = RecursosVigilancia(**serializer)
            
            recurso.new_save(usuario=request.user)
        except:
            return JsonResponse({'msj':'La vigilancia no existe'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['GET'])
    def list(self, request, *args, **kwargs):
        try:
            if Vigilancia.objects.get(id=kwargs["vigilancia_id"]):
                if request.GET.get("fecha"):
                    recursos = RecursosVigilanciaSerializer(RecursosVigilancia.objects.filter(fk_vigilancia=kwargs["vigilancia_id"], fecha=request.GET["fecha"]), many=True).data
                else:
                    recursos = RecursosVigilanciaSerializer(RecursosVigilancia.objects.filter(fk_vigilancia=kwargs["vigilancia_id"]), many=True).data
                if recursos != []:
                    resp=[]
                    for dato in recursos:
                        recurso={}
                        recurso["id"] = dato["id"]
                        recurso["recurso"] = TipoRecurso.objects.get(id=dato["fk_tipo_recurso"]).tipo_recurso
                        recurso["fecha"]  = dato["fecha"]
                        recurso["cantidad"] = dato["cantidad"]
                        resp.append(recurso)
                    return JsonResponse(resp, status=status.HTTP_200_OK)
                return JsonResponse({"error":"La vigilancia no tiene recursos asignados"}, status=status.HTTP_403_FORBIDDEN)
        except:
            return JsonResponse({"error":f"La vigilancia de ID: {kwargs['vigilancia_id']} no existe"}, status=status.HTTP_404_NOT_FOUND)


    @action(detail=True, methods=['PUT'])
    def update(self, request, *args, **kwargs):
        try:
            if Vigilancia.objects.get(id=kwargs["vigilancia_id"]):
                recurso = RecursosVigilancia.objects.get(id=kwargs["pk"])
                if recurso:
                    recurso.fk_tipo_recurso = request.POST["fk_tipo_recurso"]
                    recurso.fk_vigilancia = request.POST["fk_vigilancia"]
                    recurso.cantidad = request.POST["cantidad"]
                    recurso.save(request.user)
                    JsonResponse({"msj":"El recurso se modifico correctamente"}, status=status.HTTP_200_OK)
                return JsonResponse({"msj":"No existe el registro de recursos."}, status=status.HTTP_404_NOT_FOUND)
        except:
            return JsonResponse({"msj":"La vigilancia no existe."}, status=status.HTTP_404_NOT_FOUND)
        return super().update(request, *args, **kwargs)


class TurnosVigilanciaViewSet(DynamicModelViewSet):
    queryset = TurnosVigilancia.objects.all()
    serializer_class = TurnosVigilanciaSerializer
    
    @action(detail=True, methods=['GET'])
    def  list(self, request, *args, **kwargs):
        turnoVigilancia = TurnosVigilanciaSerializer(TurnosVigilancia.objects.get(fk_vigilancia=kwargs["vigilancia_id"])).data
        turnos = []
        for fecha in turnoVigilancia["turno"]:
            if not PersonalVigilancia.objects.filter(fecha=fecha).first():
                turnos.append(fecha)
        turnoVigilancia["turno"] = turnos
        respuesta = turnoVigilancia
        return JsonResponse(respuesta, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def retrieve(self, request, *args, **kwargs):
        turnoVigilancia = TurnosVigilanciaSerializer(TurnosVigilancia.objects.get(id=kwargs["pk"])).data
        del(turnoVigilancia["id"])
        del(turnoVigilancia["fk_vigilancia"])
        fecha=request.GET.get("fecha")
        if fecha:
            if fecha in turnoVigilancia["turno"]:
                turnoVigilancia["fecha"] = fecha
                turnoVigilancia["personal_asignado"] = False
                if PersonalVigilancia.objects.filter(fecha=fecha).first():
                    turnoVigilancia["personal_asignado"] = True
                del(turnoVigilancia["turno"])
            else:
                return JsonResponse({},status=status.HTTP_404_NOT_FOUND)
        # else:
        #     for fecha in turnoVigilancia["turno"]:
        #         if not PersonalVigilancia.objects.filter(fecha=fecha).first():
        #             turnos.append(fecha)
        #     turnoVigilancia["turno"] = turnos
        respuesta = turnoVigilancia
        return JsonResponse(respuesta, status=status.HTTP_200_OK)

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
                fechas = [x for x in fechas if x.strftime("%A") in dias_semana]
            fecha_actual += timedelta(days=1)

        for fecha in fechas:
            fechas_seleccionadas.append(str(fecha)[:10])

        return fechas_seleccionadas

    @action(detail=True, methods=['POST'])
    def create(self, request, *args, **kwargs):
        serializer = TurnosVigilanciaSerializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        vigilancia = Vigilancia.objects.get(id=kwargs["vigilancia_id"])

        fechas = self.seleccionar_fechas(
            vigilancia.fecha_inicio,
            vigilancia.fecha_fin,
            serializer.validated_data["diario"],
            serializer.validated_data["turno"],
        )

        if serializer.validated_data["dia_completo"]:
            serializer.validated_data["hora_inicio"] = "08:00:00"
            serializer.validated_data["hora_fin"] = "08:00:00"
            serializer.validated_data["duracion"] = 24
        else:
            serializer.validated_data["hora_fin"] = (
                datetime.combine(date.today(), serializer.validated_data["hora_inicio"])
                + timedelta(hours=serializer.validated_data["duracion"])
            ).time()
        try:
            turno_vigilancia = TurnosVigilancia()
            turno_vigilancia.fk_vigilancia=serializer.validated_data["fk_vigilancia"]
            turno_vigilancia.turno=fechas
            turno_vigilancia.hora_inicio=serializer.validated_data["hora_inicio"]
            turno_vigilancia.hora_fin=serializer.validated_data["hora_fin"]
            turno_vigilancia.duracion=serializer.validated_data["duracion"]
            turno_vigilancia.diario=serializer.validated_data["diario"]
            turno_vigilancia.dia_completo=serializer.validated_data["dia_completo"]
            turno_vigilancia.new_save(usuario=request.user)
            
            vigilancia.turno_asignado = True
            vigilancia.cant_dias = len(fechas)
            vigilancia.save(usuario=request.user)

            respuesta = {"msj": "Turnos Asignados Correctamente!!!"}
            return JsonResponse(respuesta, safe=False, status=status.HTTP_201_CREATED)
        except ValueError:
            respuesta = {"error": "Error al crear los Turnos"}
            return JsonResponse(
                respuesta, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=True, methods=['PATCH'])
    def partial_update(self, request, *args, **kwargs):
        turnoVigilancia =TurnosVigilanciaSerializer(TurnosVigilancia.objects.get(fk_vigilancia=kwargs['vigilancia_id'])).data
        turnoVigilancia=request.data
        serializer = TurnosVigilancia(data = turnoVigilancia, partial=True)
        if serializer.is_valid():
            turnos_vigilancia = TurnosVigilancia(**serializer.validated_data)
            turnos_vigilancia.save(request.user)
            return JsonResponse({"msj":'Turno Modificado correctamente!!'},status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonalVigilanciaViewSet(DynamicModelViewSet):
    queryset = PersonalVigilancia.objects.all()
    serializer_class = PersonalVigilanciaSerializer

    @action(detail=True, methods=['GET'])
    def list(self, *args, **kwargs):
        self.queryset = self.get_queryset()
        try:
            vigilancia = Vigilancia.objects.get(id=kwargs["vigilancia_id"]).id
            try:
                turnos_vigilancia = TurnosVigilanciaSerializer(TurnosVigilancia.objects.get(fk_vigilancia=vigilancia)).data
                try:
                    turnos = {}
                    turnos["fk_vigilancia"] = turnos_vigilancia["fk_vigilancia"]
                    turnos["turnos"] = []
                    for fecha in turnos_vigilancia["turno"]:
                        horarios = {}
                        personal_vigilancia = PersonalVigilanciaSerializer(PersonalVigilancia.objects.filter(fecha=fecha), many=True).data
                        if personal_vigilancia:
                            # horarios[fecha] = []
                            horarios = []
                            personal = []
                            for turno in personal_vigilancia:
                                fk_personal = PersonalSerializer(Personal.objects.get(legajo=turno["fk_personal"])).data
                                personal.append(
                                    {
                                        "legajo": fk_personal["legajo"],
                                        "nombre": Persona.objects.get(cuil=fk_personal["fk_persona"]).nombre_apellido,
                                    }
                                )
                                # persona['hora_inicio'] = turno['hora_inicio']
                                # persona['hora_fin'] = turno['hora_fin']
                            persona = {}
                            persona["id"] = turno["id"]
                            persona["fecha"] = fecha
                            persona["duracion"] = turno["duracion"]
                            persona["personal"] = personal
                            horarios.append(persona)
                            # horarios[fecha].append(persona)
                            turnos["turnos"].append(horarios)
                    return JsonResponse(turnos, status=status.HTTP_200_OK)
                except:
                    return JsonResponse(
                        {"msj": "La vigilancia no tiene ningun personal asignado"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            except:
                return JsonResponse(
                    {"msj": "La vigilancia no tiene ningun turnos asignado"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except:
            return JsonResponse(
                {"msj": "La vigilancia no existe"}, status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=True, methods=['POST'])
    def create(self, request, *args, **kwargs):
        fk_vigilancia = kwargs["vigilancia_id"]

        turno = TurnosVigilancia.objects.get(fk_vigilancia=fk_vigilancia)
        serializer = TurnosVigilanciaSerializer(turno)

        fk_turnoVigilancia = serializer.data["id"]

        datos_agregar = []

        fecha = request.data["fecha"]

        for contenido in request.data["turnos"]:
            personal_vigilancia = {}

            personal_vigilancia["fecha"] = fecha

            for clave, valor in dict(contenido).items():
                if clave != "":
                    if clave == "legajo":
                        personal_vigilancia["fk_personal"] = valor
                    else:
                        personal_vigilancia[clave] = valor

            if personal_vigilancia["hora_inicio"] != "":
                personal_vigilancia["fk_turnoVigilancia"] = fk_turnoVigilancia

                if personal_vigilancia["fk_personal"]:
                    personal_vigilancia["asignado"] = True
                else:
                    personal_vigilancia["asignado"] = False

                hora_inicio = datetime.strptime(personal_vigilancia["hora_inicio"], "%H:%M").time()
                hora_fin = (datetime.combine(date.today(), hora_inicio)+ timedelta(hours=personal_vigilancia["duracion"])).time()

                personal_vigilancia["hora_fin"] = hora_fin.strftime("%H:%M")
                datos_agregar.append(personal_vigilancia)

        for dato in datos_agregar:
            serializer = PersonalVigilanciaSerializer(data=dato)
            serializer.is_valid(raise_exception=True)
            personal_vigilancia = PersonalVigilancia(**serializer.validated_data)
            personal_vigilancia.new_save(request.user)
        return JsonResponse(
            {"msj": "Personal Asignado Correctamente"}, status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=['PUT'])
    def update(self, request, pk=None):
        personalVigilancia = self.get_object(pk)
        serializer = PersonalVigilancia(data=personalVigilancia)
        if serializer.data["fk_personal"]:
            if request.data["fk_personal"] != serializer.data["fk_personal"].id:
                if request.data["fk_personal"]:
                    serializer.data["fk_personal"] = Personal.objects.get(id=request.data["fk_personal"])
                else:
                    serializer.data["fk_personal"] = None
                    serializer.data["asignado"] = False
                personal_vigilancia = PersonalVigilancia(**serializer.data)
                personal_vigilancia.save(request.user)
        return JsonResponse(
            {"msj": "Turno Modificado correctamente!!"}, status=status.HTTP_200_OK
        )
