from django.urls import path
from .views import LeyViewSet, ArticuloViewSet, IncisoViewSet

urlpatterns = [
    # Leyes
    path(
        "leyes/",
        LeyViewSet.as_view({"get": "list", "post": "create"}),
        name="leyes-list",
    ),
    path(
        "leyes/<int:pk>/",
        LeyViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail-leyes",
    ),
    # Articulos
    path(
        "articulos/",
        ArticuloViewSet.as_view({"get": "list", "post": "create"}),
        name="articulos-list",
    ),
    path(
        "articulos/<int:pk>/",
        ArticuloViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail-articulos",
    ),
    # Incisos
    path(
        "incisos/",
        IncisoViewSet.as_view({"get": "list", "post": "create"}),
        name="incisos-list",
    ),
    path(
        "incisos/<int:pk>/",
        IncisoViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_incisos",
    ),
]

# urlpatterns = router.urls
