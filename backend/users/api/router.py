from django.urls import path
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.api.views import (
    UserApiViewSet, UserView, EmpleadoApiViewSet, EmpleadoCreateAPIView, EmpleadoUsuarioIdListApiView)

router_user = DefaultRouter()

# router_user.register(
#     prefix='users', basename='users', viewset=UserApiViewSet
# )
router_user.register(
    prefix="empleados", basename="empleados", viewset=EmpleadoApiViewSet
)

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/me/', UserView.as_view()),
    path("crear_empleado/", EmpleadoCreateAPIView.as_view(), name="crear empleado"),
    path("empleado_usuario/<id_usuario>/", EmpleadoUsuarioIdListApiView.as_view(), name="Obtener empleado mediando id de usuario",
         ),
]
