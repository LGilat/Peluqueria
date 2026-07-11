from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import (
    ClienteSerializer,
    ProveedorSerializer,
    ProductoSerializer,
    StockSerializer,
    ReservaSerializer,
    AtendenteSerializer,
    FacturaSerializer,
    PromocionSerializer,
    IngresoSerializer,
    GastoSerializer,
)
from .models import (
    Cliente,
    Proveedor,
    Producto,
    Stock,
    Reserva,
    Atendente,
    Factura,
    Promocion,
    Ingreso,
    Gasto,
)


# --- Cliente Views ---
class ClienteList(APIView):
    def get(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Cliente, pk=pk)

    def get(self, request, pk):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    def put(self, request, pk):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cliente = self.get_object(pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- Proveedor Views ---
class ProveedorList(APIView):
    def get(self, request):
        proveedores = Proveedor.objects.all()
        serializer = ProveedorSerializer(proveedores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProveedorDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Proveedor, pk=pk)

    def get(self, request, pk):
        proveedor = self.get_object(pk)
        serializer = ProveedorSerializer(proveedor)
        return Response(serializer.data)

    def put(self, request, pk):
        proveedor = self.get_object(pk)
        serializer = ProveedorSerializer(proveedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        proveedor = self.get_object(pk)
        proveedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- Producto Views ---
class ProductoList(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductoDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Producto, pk=pk)

    def get(self, request, pk):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

    def put(self, request, pk):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        producto = self.get_object(pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- Stock Views ---
class StockList(APIView):
    def get(self, request):
        stock = Stock.objects.all()
        serializer = StockSerializer(stock, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Stock, pk=pk)

    def get(self, request, pk):
        stock = self.get_object(pk)
        serializer = StockSerializer(stock)
        return Response(serializer.data)

    def put(self, request, pk):
        stock = self.get_object(pk)
        serializer = StockSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        stock = self.get_object(pk)
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- Reserva Views ---
class ReservaList(APIView):
    def get(self, request):
        reservas = Reserva.objects.all()
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReservaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservaDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Reserva, pk=pk)

    def get(self, request, pk):
        reserva = self.get_object(pk)
        serializer = ReservaSerializer(reserva)
        return Response(serializer.data)

    def put(self, request, pk):
        reserva = self.get_object(pk)
        serializer = ReservaSerializer(reserva, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reserva = self.get_object(pk)
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- Atendente Views ---
class AtendenteList(APIView):
    def get(self, request):
        atendentes = Atendente.objects.all()
        serializer = AtendenteSerializer(atendentes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AtendenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AtendenteDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Atendente, pk=pk)

    def get(self, request, pk):
        atendente = self.get_object(pk)
        serializer = AtendenteSerializer(atendente)
        return Response(serializer.data)

    def put(self, request, pk):
        atendente = self.get_object(pk)
        serializer = AtendenteSerializer(atendente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        atendente = self.get_object(pk)
        atendente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- Factura Views ---
class FacturaList(APIView):
    def get(self, request):
        facturas = Factura.objects.all()
        serializer = FacturaSerializer(facturas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FacturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FacturaDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Factura, pk=pk)

    def get(self, request, pk):
        factura = self.get_object(pk)
        serializer = FacturaSerializer(factura)
        return Response(serializer.data)

    def put(self, request, pk):
        factura = self.get_object(pk)
        serializer = FacturaSerializer(factura, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        factura = self.get_object(pk)
        factura.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- Promocion Views ---
class PromocionList(APIView):
    def get(self, request):
        promociones = Promocion.objects.all()
        serializer = PromocionSerializer(promociones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PromocionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PromocionDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Promocion, pk=pk)

    def get(self, request, pk):
        promocion = self.get_object(pk)
        serializer = PromocionSerializer(promocion)
        return Response(serializer.data)

    def put(self, request, pk):
        promocion = self.get_object(pk)
        serializer = PromocionSerializer(promocion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        promocion = self.get_object(pk)
        promocion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- Ingreso Views ---
class IngresoList(APIView):
    def get(self, request):
        ingresos = Ingreso.objects.all()
        serializer = IngresoSerializer(ingresos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IngresoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IngresoDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Ingreso, pk=pk)

    def get(self, request, pk):
        ingreso = self.get_object(pk)
        serializer = IngresoSerializer(ingreso)
        return Response(serializer.data)

    def put(self, request, pk):
        ingreso = self.get_object(pk)
        serializer = IngresoSerializer(ingreso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ingreso = self.get_object(pk)
        ingreso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- Gasto Views ---
class GastoList(APIView):
    def get(self, request):
        gastos = Gasto.objects.all()
        serializer = GastoSerializer(gastos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GastoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GastoDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Gasto, pk=pk)

    def get(self, request, pk):
        gasto = self.get_object(pk)
        serializer = GastoSerializer(gasto)
        return Response(serializer.data)

    def put(self, request, pk):
        gasto = self.get_object(pk)
        serializer = GastoSerializer(gasto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        gasto = self.get_object(pk)
        gasto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
