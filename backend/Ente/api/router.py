from rest_framework import routers
from .views import EnteViewSet

router = routers.DefaultRouter()

# [GET] [POST] api/ente/
# [UPDATE] [DELETE] api/ente/{id}
router.register('ente', EnteViewSet, 'ente')

urlpatterns = router.urls