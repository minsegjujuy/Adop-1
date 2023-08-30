from django.urls import path
from rest_framework import routers
from .views import (
    InspectoraViewSet,
    UnidadRegionalViewSet,
    DependenciaViewSet,
    DependenciasOperativosiewSet,
)

router = routers.DefaultRouter()

# [GET] [POST] api/dependencias_operativos/
# [UPDATE] [DELETE] api/dependencias_operativos/{id}
# router.register(
#     "dependencias_operativos", DependenciasOperativosiewSet, "dependencias_operativos"
# )

urlpatterns = [
    # Inspectoras
    path(
        "inspectoras/",
        InspectoraViewSet.as_view({"get": "list", "post": "create"}),
        name="inspectora",
    ),
    path(
        "inspectoras/<int:pk>/",
        InspectoraViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_inspectora",
    ),
    # Unidades Regionales
    path(
        "unidades_regionales/",
        UnidadRegionalViewSet.as_view({"get": "list", "post": "create"}),
        name="unidad_regional",
    ),
    path(
        "unidades_regionales/<int:pk>/",
        UnidadRegionalViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_unidad_regional",
    ),
    # Dependencias
    path(
        "dependencias/",
        DependenciaViewSet.as_view({"get": "list", "post": "create"}),
        name="dependencia",
    ),
    path(
        "dependencias/<int:pk>/",
        DependenciaViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_dependencia",
    ),
]

