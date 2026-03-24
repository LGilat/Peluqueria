from django.urls import path
from .views import AtendenteList, AtendenteDetail

urlpatterns = [
    path('', AtendenteList.as_view(), name='atendente-list'),
    path('<int:pk>/', AtendenteDetail.as_view(), name='atendente-detail'),
]
