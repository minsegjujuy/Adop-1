from rest_framework import routers
from .views import TipoServicioViewSet,ServicioViewSet, RecursoViewSet

router = routers.DefaultRouter()

# [GET] [POST] api/tipos_servicios/
# [UPDATE] [DELETE] api/tipos_servicios/{id}
router.register('api/tipos_servicios', TipoServicioViewSet, 'tipos_servicios')
# [GET] [POST] api/servicios/
# [UPDATE] [DELETE] api/servicios/{id}
router.register('api/servicios', ServicioViewSet, 'servicios')
# [GET] [POST] api/recursos/
# [UPDATE] [DELETE] api/recursos/{id}
router.register('api/recursos', RecursoViewSet, 'recursos')

urlpatterns = router.urls