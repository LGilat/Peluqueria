from rest_framework import serializers
from gestion_peluqueria.models import Cliente, Proveedor, Stock, Producto



class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'
        

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
        
class ProductoSerializer(serializers.ModelSerializer):
    stock = StockSerializer(read_only=True)
    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'descripcion', 'precio', 'imagen', 'stock')