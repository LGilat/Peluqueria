from rest_framework.routers import DefaultRouter
from .views import ReservaViewSet, HistorialReservaViewSet

router = DefaultRouter()
router.register(r'reserva', ReservaViewSet, basename='reserva')
router.register(r'historial-reserva', HistorialReservaViewSet, basename='historial-reserva')

urlpatterns = router.urls
