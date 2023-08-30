from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


class DynamicModelViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, TokenAuthentication)
    queryset = None
    serializer_class = None

    @action(detail=True, methods=["get"])
    def list(self, request, *args, **kwargs):
        datos = self.get_queryset().exclude(is_deleted=True)
        serializer = self.get_serializer(datos, many=True)
        return JsonResponse(serializer.data, safe=False)

    @action(detail=True, methods=["post"])
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data["is_deleted"]:
            return JsonResponse(
                {"detail": "No se encuentra el elemento."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer.new_save(usuario=request.user)
        return JsonResponse(
            {"msj": "Dependencia creada correctamente"}, status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=["get"])
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_deleted:
            return JsonResponse(
                {"detail": "No se encuentra el elemento."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    @action(detail=True, methods=["patch", "put"])
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_deleted:
            return JsonResponse(
                {"detail": "No se encuentra el elemento."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if request.user.is_authenticated:
            serializer.save(usuario=request.user)
        else:
            serializer.save()
        return JsonResponse(
            {"msj": "Elemento actualizado correctamente"}, status=status.HTTP_200_OK
        )

    @action(detail=True, methods=["delete"])
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_deleted:
            return JsonResponse(
                {"detail": "No se encuentra el elemento."},
                status=status.HTTP_404_NOT_FOUND,
            )
        if request.user.is_authenticated:
            instance.softDelete(usuario=request.user)
        else:
            instance.softDelete()
        return JsonResponse(
            {"msj": "Elemento eliminado correctamente"},
            status=status.HTTP_204_NO_CONTENT,
        )

    @action(detail=True, methods=["post"])
    def softRestore(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_deleted:
            if request.user.is_authenticated:
                instance.softRestore(usuario=request.user)
            else:
                instance.softRestore()
            return JsonResponse(
                {"msj": "Elemento restaurado correctamente."}, status=status.HTTP_200_OK
            )
        else:
            return JsonResponse(
                {"detail": "Peticion erronea."}, status=status.HTTP_400_BAD_REQUEST
            )
