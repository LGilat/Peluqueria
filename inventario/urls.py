from django.urls import path
from .views import (
    ProductoList, ProductoDetail,
    StockList, StockDetail,
    ProveedorList, ProveedorDetail
)

urlpatterns = [
    path('producto/', ProductoList.as_view(), name='producto-list'),
    path('producto/<int:pk>/', ProductoDetail.as_view(), name='producto-detail'),
    path('stock/', StockList.as_view(), name='stock-list'),
    path('stock/<int:pk>/', StockDetail.as_view(), name='stock-detail'),
    path('proveedor/', ProveedorList.as_view(), name='proveedor-list'),
    path('proveedor/<int:pk>/', ProveedorDetail.as_view(), name='proveedor-detail'),
]
