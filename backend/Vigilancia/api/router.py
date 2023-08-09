from django.urls import path
from rest_framework import routers
from .views import (
    MotivoViewSet,
    VigilanciaViewSet,
    TurnosVigilanciaViewSet,
    PersonalVigilanciaViewSet,
    RecursosVigilanciaViewSet,
)

router = routers.DefaultRouter()

# [GET] [POST] api/motivos/
# [UPDATE] [DELETE] api/motivos/{id}
router.register("motivos", MotivoViewSet, "motivos")

# [GET] [POST] api/vigilancias/
# [UPDATE] [DELETE] api/vigilancias/{id}
router.register("vigilancias", VigilanciaViewSet, "vigilancias")

# [GET] [POST] api/vigilancia/turnos/
# [UPDATE] [DELETE] api/vigilancia/turnos/{id}
router.register("vigilancia/turnos", TurnosVigilanciaViewSet, "turnos_vigilancias")

# [GET] [POST] api/vigilancia/turnos/
# [UPDATE] [DELETE] api/vigilancia/{id}/turnos/
router.register(
    r"vigilancia/(?P<vigilancia_id>\d+)/turnos",
    PersonalVigilanciaViewSet,
    "personal_turnos_vigilancia",
)

# [GET] [POST] api/vigilancia/turnos/
# [UPDATE] [DELETE] api/vigilancia/{id}/turnos/
router.register(
    r"vigilancia/(?P<vigilancia_id>\d+)/recursos",
    RecursosVigilanciaViewSet,
    "recursos_vigilancia",
)

urlpatterns = [
    path(
        "recursos/",
        RecursosVigilanciaViewSet.as_view({"post": "create"}),
        name="recurso-create",
    ),
    path(
        "vigilancias/<int:vigilancia_id>/recursos/",
        RecursosVigilanciaViewSet.as_view({"get": "list"}),
        name="recurso-list",
    ),
    path(
        "vigilancias/<int:vigilancia_id>/recursos/<int:pk>/",
        RecursosVigilanciaViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="recurso-detail",
    ),
]

urlpatterns += router.urls
