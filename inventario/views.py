from rest_framework.viewsets import ModelViewSet
from .models import Producto, Stock, Proveedor, Servicio
from .serializers import ProductoSerializer, StockSerializer, ProveedorSerializer, ServicioSerializer


class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class ProveedorViewSet(ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class ServicioViewSet(ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
