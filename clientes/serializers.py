from rest_framework import serializers
from .models import Cliente, ClienteServicio


class ClienteServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteServicio
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    historial_servicios = ClienteServicioSerializer(many=True, read_only=True)

    class Meta:
        model = Cliente
        fields = '__all__'
