from django.urls import path
from .views import ApiInfoView

urlpatterns = [
    path('', ApiInfoView.as_view(), name='api-info'),
]
