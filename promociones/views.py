from rest_framework.viewsets import ModelViewSet
from .models import Promocion
from .serializers import PromocionSerializer


class PromocionViewSet(ModelViewSet):
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer
