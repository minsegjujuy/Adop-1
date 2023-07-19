from Tableros.settings import MEDIA_ROOT
from ..models import Documento
from .serializer import DocumentoSerializer
from django.http import JsonResponse
from os import remove as remove_file, path, makedirs
from rest_framework import viewsets, status
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from Vigilancia.models import Vigilancia

class DocumentoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    parser_classes = [FileUploadParser,]

    def list(self, request, *args, **kwargs):
        if Vigilancia.objects.filter(id=kwargs['vigilancia_id']):
            documentos = Documento.objects.filter(fk_vigilancia=kwargs['vigilancia_id'])
            if documentos:
                resp = list()
                for documento in documentos:
                    doc = {}
                    doc['id'] = documento.id
                    doc['archivo'] = documento.file.path
                    doc['nombre'] = documento.nombre
                    doc['fk_vigilancia'] = documento.fk_vigilancia.id
                    resp.append(doc)
                print(doc)
                return JsonResponse({"archivos": resp}, safe=False, status=status.HTTP_200_OK)
            return JsonResponse({"msj": 'No hay Documentos Cargados.'}, safe=False, status=status.HTTP_200_OK)
        return JsonResponse({"error": "La Vigilancia No Existe."},status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:            
            directorio = MEDIA_ROOT+f"/vigilancias/vigilancia-{kwargs['vigilancia_id']}"
            if not path.exists(directorio):
                makedirs(directorio)
            
            nombre = f"{serializer.validated_data['file'].name}.{serializer.validated_data['file'].content_type}"
            if not path.exists(f"{directorio}/{nombre}"):
                archivo = Documento()
                archivo.nombre = f"{serializer.validated_data['file'].name}.{serializer.validated_data['file'].content_type}"
                archivo.file = serializer.validated_data['file']
                archivo.fk_vigilancia = Vigilancia.objects.get(id=kwargs['vigilancia_id'])
                archivo.save()
                headers = self.get_success_headers(serializer.data)
                return JsonResponse({'msj': 'Archivo guardado correctamente!!'}, status=status.HTTP_201_CREATED, headers=headers)
            return JsonResponse({'error': 'El archivo ya está cargado en el sistema'}, status=status.HTTP_409_CONFLICT)
        except ValueError as e:
            return JsonResponse({'error': e}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            documento = Documento.objects.get(id=kwargs['pk'])
            if path.exists(str(documento.file.path)):
                remove_file(str(documento.file.path))
                documento.delete()
                return JsonResponse({"mensaje": "Archivo eliminado correctamente"}, status=200)
            else:
                return JsonResponse({"mensaje": "No se encontro el Archivo"}, status=404)
        except:
            return JsonResponse({"mensaje": "El archivo no existe"}, status=404)