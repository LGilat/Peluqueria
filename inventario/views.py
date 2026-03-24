from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Producto, Stock, Proveedor
from .serializers import ProductoSerializer, StockSerializer, ProveedorSerializer


class ProductoList(ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class StockList(ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockDetail(RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class ProveedorList(ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class ProveedorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
