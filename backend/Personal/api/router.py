from rest_framework import routers
from .views import JerarquiaViewSet, PersonalViewSet, TipoEscalafonViewSet, TipoFuncionViewSet, TipoJerarquiaViewSet

router = routers.DefaultRouter()

# [GET] [POST] api/personal/
# [UPDATE] [DELETE] api/personal/{id}
router.register('personal', PersonalViewSet, 'personal')

# [GET] [POST] api/tipo_funcion/
router.register('tipo_funcion', TipoFuncionViewSet, basename='tipo_funcion')

# [GET] [POST] api/tipo_escalafon/
router.register('tipo_escalafon', TipoEscalafonViewSet, basename='tipo_escalafon')

# [GET] [POST] api/tipo_jerarquia/
router.register('tipo_jerarquia', TipoJerarquiaViewSet, basename='tipo_jerarquia')

# [GET] [POST] api/jerarquia/
router.register('jerarquia', JerarquiaViewSet, basename='jerarquia')

urlpatterns = router.urls