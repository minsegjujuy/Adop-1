from rest_framework import routers
from .views import PersonaViewSet

router = routers.DefaultRouter()

# [GET] [POST] api/personas/
# [UPDATE] [DELETE] api/personas/{id}
router.register("personas", PersonaViewSet, "personas")

urlpatterns = router.urls
