from rest_framework import serializers
from .models import Atendente


class AtendenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atendente
        fields = '__all__'
