from ..models import Documento
from .serializer import DocumentoSerializer
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.parsers import FileUploadParser
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class DocumentoViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (JWTAuthentication,TokenAuthentication)
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    parser_classes = [FileUploadParser]

    # @action(detail=True, methods=['get'])
    # def get(self, *args, **kwargs):
    #     self.queryset=self.get_queryset()
    #     serializer = DocumentoSerializer(self.queryset, many=True)
    #     return JsonResponse(serializer,status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Obtener las direcciones de los archivos almacenados en la base de datos
        direcciones_archivos = queryset.values_list('direccion_archivo', flat=True)

        # Puedes realizar cualquier otra operación o filtrado con las direcciones de los archivos aquí
        
        return JsonResponse({'msj':direcciones_archivos},status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        archivo_cargado = serializer.validated_data['archivo']

        # Guardar el archivo en el servidor
        with open('archivos/vigilancias/' + archivo_cargado.name, 'wb') as archivo_destino:
            for chunk in archivo_cargado.chunks():
                archivo_destino.write(chunk)

        # Guardar la dirección del archivo en la base de datos
        serializer.validated_data['direccion'] = 'archivos/vigilancias/' + archivo_cargado.name
        
        self.perform_create(serializer)

        # Obtener el ID del archivo guardado    
        archivo_id = serializer.instance.id

        headers = self.get_success_headers(serializer.data)

        return JsonResponse({'archivo_id': archivo_id}, status=status.HTTP_201_CREATED, headers=headers)