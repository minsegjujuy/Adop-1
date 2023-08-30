from django.urls import path
from .views import (
    MotivoViewSet,
    VigilanciaViewSet,
    TurnosVigilanciaViewSet,
    PersonalVigilanciaViewSet,
    RecursosVigilanciaViewSet,
)

urlpatterns = [
    # Motivos
    path(
        "motivos/",
        MotivoViewSet.as_view({"get": "list", "post": "create"}),
        name="motivos_list",
    ),
    path(
        "motivos/<int:pk>/",
        MotivoViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_motivos",
    ),
    # Vigilancias
    path(
        "vigilancias/",
        VigilanciaViewSet.as_view({"get": "list", "post": "create"}),
        name="vigilancias_list",
    ),
    path(
        "vigilancias/<int:pk>/",
        VigilanciaViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_vigilancias",
    ),
    # RecursosVigiancia
    path(
        "vigilancia/recursos/",
        RecursosVigilanciaViewSet.as_view({"post": "create"}),
        name="recurso-create",
    ),
    path(
        "vigilancias/<int:vigilancia_id>/recursos/",
        RecursosVigilanciaViewSet.as_view({"get": "list"}),
        name="vigilancia-recursos",
    ),
    path(
        "vigilancias/<int:vigilancia_id>/recursos/<int:pk>/",
        RecursosVigilanciaViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="recurso-detail",
    ),
    # TurnosVigilancia
    path(
        "vigilancias/<int:vigilancia_id>/turnos/",
        TurnosVigilanciaViewSet.as_view({"get": "list", "post": "create"}),
        name="vigilancias-turnos",
    ),
    path(
        "vigilancias/<int:vigilancia_id>/turnos/<int:pk>/",
        TurnosVigilanciaViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="turnos-detail",
    ),
    # PersonalTurnosVigilancia
    path(
        "vigilancias/<int:vigilancia_id>/turnos/personal/",
        PersonalVigilanciaViewSet.as_view({"get": "list"}),
        name="vigilancias-personal",
    ),
    path(
        "vigilancias/<int:vigilancia_id>/turnos/personal/<int:pk>/",
        PersonalVigilanciaViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="personal-detail",
    ),
]
