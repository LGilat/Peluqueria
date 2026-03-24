from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, StockViewSet, ProveedorViewSet, ServicioViewSet

router = DefaultRouter()
router.register(r'producto', ProductoViewSet, basename='producto')
router.register(r'stock', StockViewSet, basename='stock')
router.register(r'proveedor', ProveedorViewSet, basename='proveedor')
router.register(r'servicio', ServicioViewSet, basename='servicio')

urlpatterns = router.urls
