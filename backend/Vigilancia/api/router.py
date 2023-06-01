from rest_framework import routers
from .views import VigilanciaViewSet, TurnosVigilanciaViewSet, MotivoViewSet, PersonalVigilanciaViewSet

router = routers.DefaultRouter()

# [GET] [POST] api/motivos/
# [UPDATE] [DELETE] api/motivos/{id}
router.register('motivos', MotivoViewSet, 'motivos')

# [GET] [POST] api/vigilancias/
# [UPDATE] [DELETE] api/vigilancias/{id}
router.register('vigilancias', VigilanciaViewSet, 'vigilancias')

# [GET] [POST] api/vigilancia/turnos/
# [UPDATE] [DELETE] api/vigilancia/turnos/{id}
router.register('vigilancia/turnos', TurnosVigilanciaViewSet, 'turnos_vigilancias')

# [GET] [POST] api/vigilancia/turnos/
# [UPDATE] [DELETE] api/vigilancia/{id}/turnos/
router.register(r'vigilancia/(?P<vigilancia_id>\d+)/turnos', PersonalVigilanciaViewSet, 'personal_turnos_vigilancia')

urlpatterns = router.urls