from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Reserva, HistorialReserva
from .serializers import ReservaSerializer, HistorialReservaSerializer


class ReservaList(ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


class ReservaDetail(RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


class HistorialReservaList(ListCreateAPIView):
    queryset = HistorialReserva.objects.all()
    serializer_class = HistorialReservaSerializer


class HistorialReservaDetail(RetrieveUpdateDestroyAPIView):
    queryset = HistorialReserva.objects.all()
    serializer_class = HistorialReservaSerializer
