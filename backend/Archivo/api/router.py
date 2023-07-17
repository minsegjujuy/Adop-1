from rest_framework import routers
from .views import DocumentoViewSet

router = routers.DefaultRouter()

# [GET] [POST] api/documento/
# [UPDATE] [DELETE] api/documento/{id}
router.register('documento', DocumentoViewSet, 'documento')

urlpatterns = router.urls