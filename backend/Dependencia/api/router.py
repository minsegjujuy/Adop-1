from rest_framework import routers
from .views import InspectoraViewSet, UnidadRegionalViewSet, DependenciaViewSet, DependenciasOperativosiewSet

router = routers.DefaultRouter()

# [GET] [POST] api/inspectoras/
# [UPDATE] [DELETE] api/inspectoras/{id}
router.register('inspectoras', InspectoraViewSet, 'inspectoras')

# [GET] [POST] api/unidades_regionales/
# [UPDATE] [DELETE] api/unidades_regionales/{id}
router.register('unidades_regionales', UnidadRegionalViewSet, 'unidades_regionales')

# [GET] [POST] api/dependencias/
# [UPDATE] [DELETE] api/dependencias/{id}
router.register('dependencias', DependenciaViewSet, 'dependencias')

# [GET] [POST] api/dependencias_operativos/
# [UPDATE] [DELETE] api/dependencias_operativos/{id}
router.register('dependencias_operativos', DependenciasOperativosiewSet, 'dependencias_operativos')

urlpatterns = router.urls