from rest_framework import routers
from .views import PersonalViewSet

router = routers.DefaultRouter()

# [GET] [POST] api/personal/
# [UPDATE] [DELETE] api/personal/{id}
router.register('personal', PersonalViewSet, 'personal')

urlpatterns = router.urls