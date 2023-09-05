from ..models import Ente
from .serializer import EnteSerializer
from BaseModel.api.views import DynamicModelViewSet

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import JsonResponse


class EnteViewSet(DynamicModelViewSet):
    queryset = Ente.objects.all()
    serializer_class = EnteSerializer
    
    # @action(detail=True, methods=["post"])
    # def create(self, request):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     inspectora = Ente(
    #         nombre=serializer.validated_data["nombre"]
    #     )
    #     if request.user.is_authenticated:
    #         inspectora.new_save(usuario=request.user)
    #     else:
    #         inspectora.new_save()
    #     return JsonResponse(
    #         {"msj": "Ente creada correctamente"}, status=status.HTTP_201_CREATED
    #     )
