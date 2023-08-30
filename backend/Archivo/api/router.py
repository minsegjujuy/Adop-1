from django.urls import path
from .views import DocumentoViewSet

# Ruta para la vista basada en clase DocumentoCreateAPIView (solo método POST)
urlpatterns = [
    path(
        "vigilancia/documentos/",
        DocumentoViewSet.as_view({"post": "create"}),
        name="documento-create",
    ),
    path(
        "vigilancias/<int:vigilancia_id>/documentos/",
        DocumentoViewSet.as_view({"get": "list"}),
        name="documento-list",
    ),
    path(
        "vigilancias/<int:vigilancia_id>/documentos/<int:pk>/",
        DocumentoViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="documento-detail",
    ),
]
