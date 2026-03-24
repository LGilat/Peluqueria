from rest_framework import serializers
from .models import Reserva, HistorialReserva


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

    def validate(self, data):
        from datetime import date

        if data['fecha'] < date.today():
            raise serializers.ValidationError("La fecha de la reserva no puede ser en el pasado.")

        fecha = data['fecha']
        hora = data['hora']
        atendente = data.get('atendente')

        if atendente:
            reservas_existentes = Reserva.objects.filter(
                fecha=fecha,
                hora=hora,
                atendente=atendente,
                estado__in=['pendiente', 'realizada']
            )

            if self.instance:
                reservas_existentes = reservas_existentes.exclude(id=self.instance.id)

            if reservas_existentes.exists():
                raise serializers.ValidationError(
                    f"El atendente {atendente.nombre} ya tiene una reserva en ese horario."
                )

        return data


class HistorialReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialReserva
        fields = '__all__'
