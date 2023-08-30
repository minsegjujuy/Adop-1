from django.urls import path
from .views import UserViewSet


urlpatterns = [
    # Usuarios
    path(
        "usuarios/",
        UserViewSet.as_view({"get": "list", "post": "create"}),
        name="usuarios_list",
    ),
    path(
        "usuarios/<int:pk>/",
        UserViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "partial_update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_usuarios",
    ),
]
