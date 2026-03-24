from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, ClienteServicioViewSet

router = DefaultRouter()
router.register(r'cliente', ClienteViewSet, basename='cliente')
router.register(r'cliente-servicio', ClienteServicioViewSet, basename='cliente-servicio')

urlpatterns = router.urls
