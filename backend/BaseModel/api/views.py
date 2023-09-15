from django.http import JsonResponse
from django.apps import apps
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


class DynamicModelViewSet(viewsets.GenericViewSet):
    models = {}
    permission_classes = (IsAuthenticated,)
    authentication_classes = (
        JWTAuthentication,
        TokenAuthentication,
    )
    queryset = None
    serializer_class = None

    def __init__(self, *args, **kwargs):
        all_models = apps.get_models()
        for model in all_models:
            self.models[model.__name__] = model._meta.app_label

    @action(detail=True, methods=["get"])
    def list(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()
        if request.GET["inactivo"] != None and request.GET["inactivo"] == True:
            datos = self.get_queryset().exclude(is_deleted=False)
        else:
            datos = self.get_queryset().exclude(is_deleted=True)
        serializer = self.get_serializer(datos, many=True)
        return JsonResponse(serializer.data, safe=False)

    @action(detail=True, methods=["post"])
    def create(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()
        instance = self.get_serializer(data=request.data)
        instance.is_valid(raise_exception=True)

        modelo = type(self).__name__[:-7]
        Modelo = apps.get_model(app_label=self.models[modelo], model_name=modelo)

        instancia = Modelo(**instance.validated_data)

        instancia.new_save(usuario=request.user)
        return JsonResponse(
            {"msj": "Elemento creado correctamente"}, status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=["get"])
    def retrieve(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()
        instance = self.get_object()
        if request.GET["inactivo"] == None or request.GET["inactivo"] == False:
            if instance.is_deleted:
                return JsonResponse(
                    {"detail": "No se encuentra el elemento."},
                    status=status.HTTP_404_NOT_FOUND,
                )
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    @action(detail=True, methods=["patch", "put"])
    def update(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()
        instance = self.get_object()
        if request.GET["inactivo"] == None or request.GET["inactivo"] == False:
            if instance.is_deleted:
                return JsonResponse(
                    {"detail": "No se encuentra el elemento."},
                    status=status.HTTP_404_NOT_FOUND,
                )

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # Guarda los datos actualizados en la instancia

        if request.user.is_authenticated:
            instance.persist(usuario=request.user)
        else:
            instance.persist()
        return JsonResponse(
            {"msj": "Elemento actualizado correctamente"}, status=status.HTTP_200_OK
        )

    @action(detail=True, methods=["delete"])
    def destroy(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()
        instance = self.get_object()
        if request.GET["inactivo"] == None or request.GET["inactivo"] == False:
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
        self.queryset = self.get_queryset()
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
