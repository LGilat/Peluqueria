from django.urls import path
from . import views

urlpatterns = [
    path('cliente/', views.ClienteList.as_view()),
    path('proveedor/', views.ProveedorList.as_view()),
]