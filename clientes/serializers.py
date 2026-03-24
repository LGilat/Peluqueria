from rest_framework import serializers
from .models import Cliente, ClienteServicio


class ClienteServicioSerializer(serializers.ModelSerializer):
    servicio_nombre = serializers.CharField(source='servicio.nombre', read_only=True)
    atendente_nombre = serializers.SerializerMethodField()

    def get_atendente_nombre(self, obj):
        if not obj.atendente:
            return None
        return f"{obj.atendente.nombre} {obj.atendente.apellido}"

    class Meta:
        model = ClienteServicio
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    historial_servicios = ClienteServicioSerializer(many=True, read_only=True)

    class Meta:
        model = Cliente
        fields = '__all__'
