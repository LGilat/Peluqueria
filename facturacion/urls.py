from django.urls import path
from .views import (
    FacturaList, FacturaDetail,
    LineaFacturaList, LineaFacturaDetail,
    IngresoList, IngresoDetail,
    GastoList, GastoDetail
)

urlpatterns = [
    path('factura/', FacturaList.as_view(), name='factura-list'),
    path('factura/<int:pk>/', FacturaDetail.as_view(), name='factura-detail'),
    path('linea-factura/', LineaFacturaList.as_view(), name='linea-factura-list'),
    path('linea-factura/<int:pk>/', LineaFacturaDetail.as_view(), name='linea-factura-detail'),
    path('ingreso/', IngresoList.as_view(), name='ingreso-list'),
    path('ingreso/<int:pk>/', IngresoDetail.as_view(), name='ingreso-detail'),
    path('gasto/', GastoList.as_view(), name='gasto-list'),
    path('gasto/<int:pk>/', GastoDetail.as_view(), name='gasto-detail'),
]
