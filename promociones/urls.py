from django.urls import path
from .views import PromocionList, PromocionDetail

urlpatterns = [
    path('promocion/', PromocionList.as_view(), name='promocion-list'),
    path('promocion/<int:pk>/', PromocionDetail.as_view(), name='promocion-detail'),
]
