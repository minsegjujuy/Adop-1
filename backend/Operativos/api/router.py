from rest_framework import routers
from .views import OperativoViewSet ,OperativoPersonalViewSet

router = routers.DefaultRouter()

# [GET] [POST] api/operativos_policiales/
# [UPDATE] [DELETE] api/operativos_policiales/{id}
router.register('api/operativos_policiales', OperativoViewSet, 'operativo_policials')

# [GET] [POST] api/policial_operativo/
# [UPDATE] [DELETE] api/policial_operativo/{id}
router.register('api/policial_operativo', OperativoPersonalViewSet, 'personal_operativo')

urlpatterns = router.urls