from rest_framework import routers
from .views import InspectoraViewSet, UnidadRegionalViewSet, DependenciaViewSet, DependenciasOperativosiewSet

router = routers.DefaultRouter()

# [GET] [POST] api/inspectoras/
# [UPDATE] [DELETE] api/inspectoras/{id}
router.register('api/inspectoras', InspectoraViewSet, 'inspectoras')

# [GET] [POST] api/unidades_regionales/
# [UPDATE] [DELETE] api/unidades_regionales/{id}
router.register('api/unidades_regionales', UnidadRegionalViewSet, 'unidades_regionales')

# [GET] [POST] api/dependencias/
# [UPDATE] [DELETE] api/dependencias/{id}
router.register('api/dependencias', DependenciaViewSet, 'dependencias')

# [GET] [POST] api/dependencias_operativos/
# [UPDATE] [DELETE] api/dependencias_operativos/{id}
router.register('api/dependencias_operativos', DependenciasOperativosiewSet, 'dependencias_operativos')

urlpatterns = router.urls