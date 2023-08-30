from django.urls import path
from .views import EnteViewSet
urlpatterns = [
    # Ente
    path(
        "ente/",
        EnteViewSet.as_view({"get": "list", "post": "create"}),
        name="ente",
    ),
    path(
        "ente/<int:pk>/",
        EnteViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_ente",
    ),
]
