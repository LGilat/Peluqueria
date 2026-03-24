from rest_framework import serializers
from .models import Atendente, NominaMensual, NominaItem, Aviso, AvisoDestinatario


class AtendenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atendente
        fields = '__all__'


class NominaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NominaItem
        fields = '__all__'


class NominaMensualSerializer(serializers.ModelSerializer):
    items = NominaItemSerializer(many=True, read_only=True)

    class Meta:
        model = NominaMensual
        fields = '__all__'


class AvisoDestinatarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvisoDestinatario
        fields = '__all__'


class AvisoSerializer(serializers.ModelSerializer):
    destinatarios = AvisoDestinatarioSerializer(many=True, read_only=True)

    class Meta:
        model = Aviso
        fields = '__all__'
