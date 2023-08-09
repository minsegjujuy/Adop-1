from rest_framework import routers
from .views import LeyViewSet, ArticuloViewSet, IncisoViewSet

router = routers.DefaultRouter()

# [GET] [POST] api/leyes/
# [UPDATE] [DELETE] api/leyes/{id}
router.register("leyes", LeyViewSet, "leyes")

# [GET] [POST] api/articulos/
# [UPDATE] [DELETE] api/articulos/{id}
router.register("articulos", ArticuloViewSet, "articulos")

# [GET] [POST] api/incisos/
# [UPDATE] [DELETE] api/incisos/{id}
router.register("incisos", IncisoViewSet, "incisos")

urlpatterns = router.urls
