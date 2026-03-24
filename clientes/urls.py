from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet

router = DefaultRouter()
router.register(r'cliente', ClienteViewSet, basename='cliente')

urlpatterns = router.urls
