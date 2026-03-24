from django.urls import path
from .views import ClienteList, ClienteDetail

urlpatterns = [
    path('', ClienteList.as_view(), name='cliente-list'),
    path('<int:pk>/', ClienteDetail.as_view(), name='cliente-detail'),
]
