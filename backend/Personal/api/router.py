from rest_framework import routers
from .views import JerarquiaViewSet, PersonalViewSet

router = routers.DefaultRouter()

# [GET] [POST] api/personal/
# [UPDATE] [DELETE] api/personal/{id}
router.register('personal', PersonalViewSet, 'personal')

# [GET] [POST] api/tipo_funcion/
# router.register('tipo_funcion', TipoFuncionViewSet, basename='tipo_funcion')

# [GET] [POST] api/jerarquia/
router.register('jerarquia', JerarquiaViewSet, basename='jerarquia')

urlpatterns = router.urls