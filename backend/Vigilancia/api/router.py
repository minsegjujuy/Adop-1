from rest_framework import routers
from .views import VigilanciaViewSet, TurnosVigilanciaViewSet, MotivoViewSet, PersonalVigilanciaViewSet

router = routers.DefaultRouter()

# [GET] [POST] api/motivos/
# [UPDATE] [DELETE] api/motivos/{id}
router.register('motivos', MotivoViewSet, 'motivos')

# [GET] [POST] api/vigilancias/
# [UPDATE] [DELETE] api/vigilancias/{id}
router.register('vigilancias', VigilanciaViewSet, 'vigilancias')

# [GET] [POST] api/dias_vigilancias/
# [UPDATE] [DELETE] api/dias_vigilancias/{id}
router.register('vigilancia/turnos', TurnosVigilanciaViewSet, 'turnos_vigilancias')

# [GET] [POST] api/turnos_vigilancia/
# [UPDATE] [DELETE] api/turnos_vigilancia/{id}
router.register('vigilancias/turnos/personal', PersonalVigilanciaViewSet, 'personal_vigilancias')

urlpatterns = router.urls