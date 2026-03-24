from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    FacturaViewSet, LineaFacturaViewSet, IngresoViewSet, GastoViewSet, FinancialReportView
)

router = DefaultRouter()
router.register(r'factura', FacturaViewSet, basename='factura')
router.register(r'linea-factura', LineaFacturaViewSet, basename='linea-factura')
router.register(r'ingreso', IngresoViewSet, basename='ingreso')
router.register(r'gasto', GastoViewSet, basename='gasto')

urlpatterns = [
    path('reportes-financieros/', FinancialReportView.as_view(), name='reportes-financieros'),
]

urlpatterns += router.urls
