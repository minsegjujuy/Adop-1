from rest_framework import routers
from .views import ProcedimientoViewSet, ProcedimientoPersonaViewSet

router = routers.DefaultRouter()

# [GET] [POST] api/procedimientos/
# [UPDATE] [DELETE] api/procedimientos/{id}
router.register('api/procedimientos', ProcedimientoViewSet, 'Procedimiento')

# [GET] [POST] api/procedimientosPersonas/
# [UPDATE] [DELETE] api/procedimientosPersonas/{id}
router.register('api/procedimientosPersonas', ProcedimientoPersonaViewSet, 'ProcedimientoPersonas')

urlpatterns = router.urls