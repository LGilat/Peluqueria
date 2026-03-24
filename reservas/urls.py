from django.urls import path
from .views import (
    ReservaList, ReservaDetail,
    HistorialReservaList, HistorialReservaDetail
)

urlpatterns = [
    path('reserva/', ReservaList.as_view(), name='reserva-list'),
    path('reserva/<int:pk>/', ReservaDetail.as_view(), name='reserva-detail'),
    path('historial-reserva/', HistorialReservaList.as_view(), name='historial-reserva-list'),
    path('historial-reserva/<int:pk>/', HistorialReservaDetail.as_view(), name='historial-reserva-detail'),
]
