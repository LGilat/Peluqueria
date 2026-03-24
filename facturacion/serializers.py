from rest_framework import serializers
from .models import Factura, LineaFactura, Ingreso, Gasto


class LineaFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineaFactura
        fields = '__all__'


class FacturaSerializer(serializers.ModelSerializer):
    lineas_factura = LineaFacturaSerializer(many=True, read_only=True)

    class Meta:
        model = Factura
        fields = '__all__'


class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingreso
        fields = '__all__'


class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = '__all__'
