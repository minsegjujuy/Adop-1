from rest_framework import routers
from .views import DocumentoViewSet

router = routers.DefaultRouter()

# [GET] [POST] api/vigilancia/{vigilancia_id}/documento/
# [UPDATE] [DELETE] api/vigilancia/{vigilancia_id}/documento/{id}
router.register(r'vigilancias/(?P<vigilancia_id>\d+)/documentos', DocumentoViewSet, 'documentos')

urlpatterns = router.urls