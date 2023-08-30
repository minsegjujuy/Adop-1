from django.urls import path
from .views import PersonaViewSet

urlpatterns = [
    # Personas
    path(
        "personas/",
        PersonaViewSet.as_view({"get": "list", "post": "create"}),
        name="personas_list",
    ),
    path(
        "personas/<int:pk>/",
        PersonaViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_personas",
    ),
]
