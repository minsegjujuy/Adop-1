from ..models import Documento
from .serializer import DocumentoSerializer
from django.http import JsonResponse
from os import remove as remove_file, path
from rest_framework import viewsets, status
from rest_framework.parsers import FileUploadParser
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from Tableros.settings import URL_ARCHIVOS
from Vigilancia.models import Vigilancia

class DocumentoViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    parser_classes = [FileUploadParser,]

    def list(self, request, *args, **kwargs):
        if Vigilancia.objects.filter(id=kwargs['vigilancia_id']):
            documentos = DocumentoSerializer(Documento.objects.filter(fk_vigilancia=kwargs['vigilancia_id']),many=True).data
            if documentos:
                return JsonResponse({"archivos": list(documentos)}, safe=False, status=status.HTTP_200_OK)
            return JsonResponse({"msj": 'No hay Documentos Cargados.'}, safe=False, status=status.HTTP_200_OK)
        return JsonResponse({"error": "La Vigilancia No Existe."},status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        serializer.validated_data['direccion']=URL_ARCHIVOS+serializer.validated_data['file'].name
        serializer.validated_data['fk_vigilancia']=Vigilancia.objects.get(id=kwargs['vigilancia_id'])
        
        if not Documento.objects.filter(direccion=serializer.validated_data['direccion']):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return JsonResponse({'msj': 'Archivo guardado correctamente!!'}, status=status.HTTP_201_CREATED, headers=headers)
        return JsonResponse({'error': 'El archivo ya está cargado en el sistema'}, status=status.HTTP_409_CONFLICT)

    def destroy(self, request, *args, **kwargs):
        documento = Documento.objects.get(id=kwargs['pk'])
        if path.exists(str(documento.file)):
            remove_file(str(documento.file))
            documento.delete()
            return JsonResponse({"mensaje": "Archivo eliminado correctamente"}, status=200)
        else:
            return JsonResponse({"mensaje": "El archivo no existe"}, status=404)