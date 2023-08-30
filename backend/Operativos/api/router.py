from django.urls import path
from .views import OperativoViewSet, OperativoPersonalViewSet

urlpatterns = [
    # Operativos
    path(
        "operativos_policiales/",
        OperativoViewSet.as_view({"get": "list", "post": "create"}),
        name="operativos_policiales_list",
    ),
    path(
        "operativos_policiales/<int:pk>/",
        OperativoViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_operativos_policiales",
    ),
    
    # Operativo-Personal
    path(
        "personal_operativo/",
        OperativoPersonalViewSet.as_view({"get": "list", "post": "create"}),
        name="personal_operativo_list",
    ),
    path(
        "personal_operativo/<int:pk>/",
        OperativoPersonalViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_personal_operativo",
    ),
]
