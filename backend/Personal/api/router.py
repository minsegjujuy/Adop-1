from django.urls import path
from .views import (
    CategoriaViewSet,
    FuncionarioViewSet,
    JerarquiaViewSet,
    PersonalViewSet,
)


urlpatterns = [
    # Personal
    path(
        "personal/",
        PersonalViewSet.as_view({"get": "list", "post": "create"}),
        name="personal_list",
    ),
    path(
        "personal/<int:pk>/",
        PersonalViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_personal",
    ),
    # Jerarquias
    path(
        "jerarquia/",
        JerarquiaViewSet.as_view({"get": "list", "post": "create"}),
        name="jerarquia_list",
    ),
    path(
        "jerarquia/<int:pk>/",
        JerarquiaViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_jerarquia",
    ),
    # Cargos
    path(
        "cargo/",
        CategoriaViewSet.as_view({"get": "list", "post": "create"}),
        name="cargo",
    ),
    path(
        "cargo/<int:pk>/",
        CategoriaViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_cargo",
    ),
    # Funcionarios
    path(
        "funcionario/",
        FuncionarioViewSet.as_view({"get": "list", "post": "create"}),
        name="funcionario_list",
    ),
    path(
        "funcionario/<int:pk>/",
        FuncionarioViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "update",
                "put": "update",
                "delete": "destroy",
                "post": "softRestore",
            }
        ),
        name="detail_funcionario",
    ),
]
