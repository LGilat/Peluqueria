from django.urls import path
from . import views

urlpatterns = [
    # Cliente URLs
    path('cliente/', views.ClienteList.as_view(), name='cliente-list'),
    path('cliente/<int:pk>/', views.ClienteDetail.as_view(), name='cliente-detail'),

    # Proveedor URLs
    path('proveedor/', views.ProveedorList.as_view(), name='proveedor-list'),
    path('proveedor/<int:pk>/', views.ProveedorDetail.as_view(), name='proveedor-detail'),

    # Producto URLs
    path('producto/', views.ProductoList.as_view(), name='producto-list'),
    path('producto/<int:pk>/', views.ProductoDetail.as_view(), name='producto-detail'),

    # Stock URLs
    path('stock/', views.StockList.as_view(), name='stock-list'),
    path('stock/<int:pk>/', views.StockDetail.as_view(), name='stock-detail'),

    # Reserva URLs
    path('reserva/', views.ReservaList.as_view(), name='reserva-list'),
    path('reserva/<int:pk>/', views.ReservaDetail.as_view(), name='reserva-detail'),

    # Atendente URLs
    path('atendente/', views.AtendenteList.as_view(), name='atendente-list'),
    path('atendente/<int:pk>/', views.AtendenteDetail.as_view(), name='atendente-detail'),

    # Factura URLs
    path('factura/', views.FacturaList.as_view(), name='factura-list'),
    path('factura/<int:pk>/', views.FacturaDetail.as_view(), name='factura-detail'),

    # Promocion URLs
    path('promocion/', views.PromocionList.as_view(), name='promocion-list'),
    path('promocion/<int:pk>/', views.PromocionDetail.as_view(), name='promocion-detail'),

    # Ingreso URLs
    path('ingreso/', views.IngresoList.as_view(), name='ingreso-list'),
    path('ingreso/<int:pk>/', views.IngresoDetail.as_view(), name='ingreso-detail'),

    # Gasto URLs
    path('gasto/', views.GastoList.as_view(), name='gasto-list'),
    path('gasto/<int:pk>/', views.GastoDetail.as_view(), name='gasto-detail'),
]
