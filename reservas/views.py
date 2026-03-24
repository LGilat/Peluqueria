from rest_framework.viewsets import ModelViewSet
from .models import Reserva, HistorialReserva
from .serializers import ReservaSerializer, HistorialReservaSerializer


class ReservaViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


class HistorialReservaViewSet(ModelViewSet):
    queryset = HistorialReserva.objects.all()
    serializer_class = HistorialReservaSerializer
