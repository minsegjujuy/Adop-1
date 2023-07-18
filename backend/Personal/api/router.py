from rest_framework import routers
from .views import CategoriaViewSet, FuncionarioViewSet, JerarquiaViewSet, PersonalViewSet

router = routers.DefaultRouter()

# [GET] [POST] api/personal/
# [UPDATE] [DELETE] api/personal/{id}
router.register('personal', PersonalViewSet, 'personal')

# [GET] [POST] api/tipo_funcion/
# router.register('tipo_funcion', TipoFuncionViewSet, basename='tipo_funcion')

# [GET] [POST] api/jerarquia/
router.register('jerarquia', JerarquiaViewSet, basename='jerarquia')

# [GET] [POST] api/cargp/
# [UPDATE] [DELETE] api/cargp/{id}
router.register('cargo', CategoriaViewSet, 'cargo')

# [GET] [POST] api/funcionario/
# [UPDATE] [DELETE] api/funcionario/{id}
router.register('funcionario', FuncionarioViewSet, 'funcionario')

urlpatterns = router.urls