from ..models import Dependencia, Inspectora, UnidadRegional, DependenciaOperativos
from .serializer import InspectoraSerializer, UnidadRegionalSerializer, DependenciaSerializer, DependenciaOperativosSerializer
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class InspectoraViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Inspectora.objects.all()    
    serializer_class = InspectoraSerializer

class UnidadRegionalViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = UnidadRegional.objects.all()    
    serializer_class = UnidadRegionalSerializer

    def list(self,request):
        self.queryset = self.get_queryset()
        usuario=request.user
        serializer =UnidadRegionalSerializer(self.queryset,many=True)
        
        if usuario.rol.rol == "OPERADOR":
            datos = [x for x in serializer.data if x['unidad_regional'] == usuario.unidad_regional.unidad_regional]
        else:
            datos = serializer.data
        
        return Response(datos)

    def create(self,request):
        self.queryset = self.get_queryset()
        usuario=request.user
        if usuario.rol.rol == "ADMINISTRADOR":
            if UnidadRegional.objects.filter(unidad_regional=request.POST.get('unidad_regional')).first() is None:
                UnidadRegional.objects.create(
                    id=len(UnidadRegional.objects.all())+1,
                    unidad_regional=request.POST.get('unidad_regional')
                )
                respuesta = {
                    'msj':'Unidad Regional creada con exito!!!'
                }
                return JsonResponse(respuesta,status=status.HTTP_201_CREATED)
            else:
                respuesta = {
                    'msj':'La Unidad Regional ingresada ya existe'
                }
                return JsonResponse(respuesta,status=status.HTTP_201_CREATED)
        else:
            respuesta = {
                "msj" : "No tiene los permisosnecesarios para realizar esta accion."
            }
            return JsonResponse(respuesta,status=status.HTTP_403_FORBIDDEN)

class DependenciaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Dependencia.objects.all()    
    serializer_class = DependenciaSerializer
    
    def list(self,request):
        self.queryset = self.get_queryset()
        usuario =request.user
        serializer = DependenciaSerializer(self.queryset, many=True)
        
        if usuario.rol.rol == 'OPERADOR':
            datos = [x for x in serializer.data if x['fk_unidad_regional'] == usuario.unidad_regional.id]
        else:
            try:
                ur = int(request.GET['uurr'])
                datos = [x for x in serializer.data if x['fk_unidad_regional'] == ur]
            except:
                datos=serializer.data
            
        respuesta = []
        
        for uurr in datos:
            data = {}
            data['id'] = uurr['id']
            data['jurisdiccion'] = uurr['jurisdiccion']
            respuesta.append(data)
        return Response(respuesta)

class DependenciasOperativosiewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = DependenciaOperativos.objects.all()    
    serializer_class = DependenciaOperativosSerializer