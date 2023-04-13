from ..models import Dependencia, Inspectora, UnidadRegional, DependenciaOperativos
from .serializer import InspectoraSerializer, UnidadRegionalSerializer, DependenciaSerializer, DependenciaOperativosSerializer
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
        usuario=request.user
        serializer =UnidadRegionalSerializer(self.queryset,many=True)
        
        if usuario.rol.rol == "OPERADOR":
            datos = [x for x in serializer.data if x['unidad_regional'] == usuario.unidad_regional.unidad_regional]
        else:
            datos = serializer.data
        
        return Response(datos)

class DependenciaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Dependencia.objects.all()    
    serializer_class = DependenciaSerializer
    
    def list(self,request):
        ur = int(request.GET.get('uurr'))
        usuario =request.user
        serializer = DependenciaSerializer(self.queryset, many=True)
        
        if usuario.rol.rol == 'OPERADOR':
            datos = [x for x in serializer.data if x['fk_unidad_regional'] == usuario.unidad_regional.id]
        else:
            # datos = [x for x in serializer.data if x['fk_unidad_regional'] == ur]
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