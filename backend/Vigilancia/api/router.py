from rest_framework import routers
from .views import VigilanciaViewSet, DiasVigilanciaViewSet, MotivoViewSet

router = routers.DefaultRouter()

# [GET] [POST] api/motivos/
# [UPDATE] [DELETE] api/motivos/{id}
router.register('motivos', MotivoViewSet, 'motivos')

# [GET] [POST] api/vigilancias/
# [UPDATE] [DELETE] api/vigilancias/{id}
router.register('vigilancias', VigilanciaViewSet, 'vigilancias')

# [GET] [POST] api/dias_vigilancias/
# [UPDATE] [DELETE] api/dias_vigilancias/{id}
router.register('dias_vigilancias', DiasVigilanciaViewSet, 'dias_vigilancias')

urlpatterns = router.urls