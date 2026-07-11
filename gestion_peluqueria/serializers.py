from rest_framework import serializers
from gestion_peluqueria.models import (
    Cliente,
    Proveedor,
    Stock,
    Producto,
    Reserva,
    Atendente,
    Factura,
    LineaFactura,
    Ingreso,
    Gasto,
    Promocion,
    HistorialReserva,
)


# --- Cliente Serializer ---
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


# --- Proveedor Serializer ---
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'


# --- Producto Serializer ---
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


# --- Stock Serializer ---
class StockSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    proveedor = ProveedorSerializer(read_only=True)

    class Meta:
        model = Stock
        fields = '__all__'


# --- Atendente Serializer ---
class AtendenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atendente
        fields = '__all__'


# --- Reserva Serializer ---
class ReservaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    atendente = AtendenteSerializer(read_only=True)

    class Meta:
        model = Reserva
        fields = '__all__'


# --- HistorialReserva Serializer ---
class HistorialReservaSerializer(serializers.ModelSerializer):
    reserva = ReservaSerializer(read_only=True)

    class Meta:
        model = HistorialReserva
        fields = '__all__'


# --- Factura Serializer ---
class FacturaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    promocion = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Factura
        fields = '__all__'


# --- LineaFactura Serializer ---
class LineaFacturaSerializer(serializers.ModelSerializer):
    factura = FacturaSerializer(read_only=True)
    producto = ProductoSerializer(read_only=True)

    class Meta:
        model = LineaFactura
        fields = '__all__'


# --- Ingreso Serializer ---
class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingreso
        fields = '__all__'


# --- Gasto Serializer ---
class GastoSerializer(serializers.ModelSerializer):
    proveedor = ProveedorSerializer(read_only=True)

    class Meta:
        model = Gasto
        fields = '__all__'


# --- Promocion Serializer ---
class PromocionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocion
        fields = '__all__'
