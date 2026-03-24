from rest_framework.routers import DefaultRouter
from .views import AtendenteViewSet

router = DefaultRouter()
router.register(r'atendente', AtendenteViewSet, basename='atendente')

urlpatterns = router.urls
