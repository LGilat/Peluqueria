from rest_framework.viewsets import ModelViewSet
from .models import Factura, LineaFactura, Ingreso, Gasto
from .serializers import FacturaSerializer, LineaFacturaSerializer, IngresoSerializer, GastoSerializer


class FacturaViewSet(ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer


class LineaFacturaViewSet(ModelViewSet):
    queryset = LineaFactura.objects.all()
    serializer_class = LineaFacturaSerializer


class IngresoViewSet(ModelViewSet):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer


class GastoViewSet(ModelViewSet):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer
