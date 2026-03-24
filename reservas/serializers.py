from datetime import datetime, timedelta
from rest_framework import serializers
from .models import Reserva, HistorialReserva


class ReservaSerializer(serializers.ModelSerializer):
    servicio_detalle = serializers.StringRelatedField(source='servicio', read_only=True)

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
        servicio = data.get('servicio')

        if atendente and servicio:
            reservas_existentes = Reserva.objects.filter(
                fecha=fecha,
                atendente=atendente,
                estado__in=['pendiente', 'realizada', 'finalizada']
            ).select_related('servicio')

            if self.instance:
                reservas_existentes = reservas_existentes.exclude(id=self.instance.id)

            start = datetime.combine(fecha, hora)
            end = start + timedelta(minutes=servicio.duracion_minutos)

            for reserva in reservas_existentes:
                existing_start = datetime.combine(reserva.fecha, reserva.hora)
                existing_end = existing_start + timedelta(minutes=reserva.servicio.duracion_minutos)
                if existing_start < end and start < existing_end:
                    raise serializers.ValidationError(
                        f"El atendente {atendente.nombre} ya tiene una reserva en ese horario."
                    )

        return data


class HistorialReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialReserva
        fields = '__all__'
