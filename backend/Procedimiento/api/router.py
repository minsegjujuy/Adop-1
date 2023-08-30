from django.urls import path
from .views import ProcedimientoViewSet, ProcedimientoPersonaViewSet

urlpatterns = [
    # Procedimientos
    path(
        "procedimiento/",
        ProcedimientoViewSet.as_view({"get": "list", "post": "create"}),
        name="procedimientos_list",
    ),
    path(
        "procedimiento/<int:pk>/",
        ProcedimientoViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_procedimiento",
    ),
    # Procedimiento Personas
    path(
        "procedimiento_personas/",
        ProcedimientoPersonaViewSet.as_view({"get": "list", "post": "create"}),
        name="procedimiento_personas",
    ),
    path(
        "procedimiento_personas/<int:pk>/",
        ProcedimientoPersonaViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_procedimiento_personas",
    ),
]
