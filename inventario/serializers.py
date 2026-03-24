from rest_framework import serializers

from .models import Producto, Stock, Proveedor, Servicio


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    stock = StockSerializer(many=True, read_only=True, source='stocks')

    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'descripcion', 'precio', 'imagen', 'stock')


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'
