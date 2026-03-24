from rest_framework.routers import DefaultRouter
from .views import (
    AtendenteViewSet,
    NominaMensualViewSet,
    NominaItemViewSet,
    AvisoViewSet,
    AvisoDestinatarioViewSet,
)

router = DefaultRouter()
router.register(r'atendente', AtendenteViewSet, basename='atendente')
router.register(r'nomina', NominaMensualViewSet, basename='nomina')
router.register(r'nomina-item', NominaItemViewSet, basename='nomina-item')
router.register(r'aviso', AvisoViewSet, basename='aviso')
router.register(r'aviso-destinatario', AvisoDestinatarioViewSet, basename='aviso-destinatario')

urlpatterns = router.urls
