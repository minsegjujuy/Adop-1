from rest_framework import routers
from .views import SecuestroViewSet, TipoSecuestroViewSet

router = routers.DefaultRouter()

# [GET] [POST] api/tipos_secuestros/
# [UPDATE] [DELETE] api/tipos_secuestros/{id}
router.register('api/tipos_secuestros', TipoSecuestroViewSet, 'tipos_secuestros')
# [GET] [POST] api/secuestros/
# [UPDATE] [DELETE] api/secuestros/{id}
router.register('api/secuestros', SecuestroViewSet, 'secuestros')

urlpatterns = router.urls