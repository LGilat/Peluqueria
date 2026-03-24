from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Factura, LineaFactura, Ingreso, Gasto
from .serializers import FacturaSerializer, LineaFacturaSerializer, IngresoSerializer, GastoSerializer


class FacturaList(ListCreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer


class FacturaDetail(RetrieveUpdateDestroyAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer


class LineaFacturaList(ListCreateAPIView):
    queryset = LineaFactura.objects.all()
    serializer_class = LineaFacturaSerializer


class LineaFacturaDetail(RetrieveUpdateDestroyAPIView):
    queryset = LineaFactura.objects.all()
    serializer_class = LineaFacturaSerializer


class IngresoList(ListCreateAPIView):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer


class IngresoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer


class GastoList(ListCreateAPIView):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer


class GastoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer
