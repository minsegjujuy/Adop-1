from Tableros.settings import MEDIA_ROOT
from ..models import Documento
from .serializer import DocumentoSerializer
from django.http import JsonResponse
from os import remove as remove_file, path, makedirs
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from Vigilancia.models import Vigilancia

class DocumentoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

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
                return JsonResponse({"archivos": resp}, safe=False, status=status.HTTP_200_OK)
            return JsonResponse({"msj": 'No hay Documentos Cargados.'}, safe=False, status=status.HTTP_200_OK)
        return JsonResponse({"error": "La Vigilancia No Existe."},status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            try:
                Vigilancia.objects.get(id=kwargs['vigilancia_id'])
                try:
                    resp = {}
                    documento = Documento.objects.get(id=kwargs['pk'])
                    resp['archivo'] = documento.file.path
                    resp['nombre'] = documento.nombre
                    del documento
                    return JsonResponse(resp, safe=False, status=status.HTTP_200_OK)
                except:
                    return JsonResponse({"error": "No existe el documento."})
            except:
                return JsonResponse({"error": f"No existe la vigilancia de ID: {kwargs['vigilancia_id']}."})
        except ValueError as e:
            return JsonResponse({"error": e},status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request, *args, **kwargs):
        files = request.data.getlist('file')
        fk_vigilancia = request.data.get('fk_vigilancia')
        directorio = f"{MEDIA_ROOT}/vigilancias/vigilancia-{fk_vigilancia}"

        if not path.exists(directorio):
            makedirs(directorio)

        errors = ""
        for file in files:
            nombre = f"{file.name.split('.')[0]}.{file.content_type.split('/')[1]}"
            if not path.exists(f"{directorio}/{nombre}"):
                archivo = Documento(nombre=nombre, file=file, fk_vigilancia_id=fk_vigilancia)
                archivo.save()
            else:
                errors = errors + nombre + ', '

        if errors:
            return JsonResponse({'error': f'Los archivos {errors}ya estan cargados en el sistema.'}, status=status.HTTP_409_CONFLICT)

        headers = self.get_success_headers()
        return JsonResponse({'msj': 'Archivo/s guardado/s correctamente!!'}, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        try:
            direccion = MEDIA_ROOT+f"/vigilancias/vigilancia-{kwargs['vigilancia_id']}"
            if path.exists(direccion):
                documento = Documento.objects.get(id=kwargs['pk'])
                if path.exists(documento.file.path):
                    if not path.exists(f"{direccion}/{request.FILES['file'].name}"):
                        remove_file(documento.file.path)
                    else:
                        return JsonResponse({'error':'Este archivo ya esta cargado en el sistema'},status=status.HTTP_403_FORBIDDEN)
                archivo = request.FILES['file']
                documento.file = archivo
                documento.nombre = archivo.name
                documento.save()
                return JsonResponse({'msj': 'Archivo Modificado correctamente'}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({'error': f"El archivo no existe en la vigilancia {kwargs['vigilancia_id']}"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            return JsonResponse({'error':e}, status=status.HTTP_400_BAD_REQUEST)

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