from django.urls import path
from .views import SecuestroViewSet, TipoSecuestroViewSet

urlpatterns = [
    # Tipos de Secuestro
    path(
        "tipos_secuestro/",
        TipoSecuestroViewSet.as_view({"get": "list", "post": "create"}),
        name="tipos_secuestros_list",
    ),
    path(
        "tipos_secuestro/<int:pk>/",
        TipoSecuestroViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_tipos_secuestro",
    ),
    # Secuestros
    path(
        "secuestros/",
        SecuestroViewSet.as_view({"get": "list", "post": "create"}),
        name="secuestros_list",
    ),
    path(
        "secuestros/<int:pk>/",
        SecuestroViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_secuestro",
    ),
]
