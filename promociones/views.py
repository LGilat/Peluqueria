from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Promocion
from .serializers import PromocionSerializer


class PromocionList(ListCreateAPIView):
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer


class PromocionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer
