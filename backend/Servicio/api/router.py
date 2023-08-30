from django.urls import path
from .views import TipoServicioViewSet, ServicioViewSet, RecursoViewSet

urlpatterns = [
    # Tipos de Servicio
    path(
        "tipo_servicio/",
        TipoServicioViewSet.as_view({"get": "list", "post": "create"}),
        name="tipo_servicios_list",
    ),
    path(
        "tipo_servicio/<int:pk>/",
        TipoServicioViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_tipo_servicio",
    ),
    # Servicios
    path(
        "servicios/",
        ServicioViewSet.as_view({"get": "list", "post": "create"}),
        name="servicios_list",
    ),
    path(
        "servicios/<int:pk>/",
        ServicioViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_servicios",
    ),
    # Recursos
    path(
        "recursos/",
        RecursoViewSet.as_view({"get": "list", "post": "create"}),
        name="recursos_list",
    ),
    path(
        "recursos/<int:pk>/",
        RecursoViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_recursos",
    ),
]
