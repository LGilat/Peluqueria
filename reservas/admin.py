from django.contrib import admin
from .models import Reserva, HistorialReserva


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'cliente', 'servicio', 'fecha', 'hora', 'estado', 'atendente',
        'recordatorio_enviado'
    )
    search_fields = ('cliente__nombre', 'cliente__apellido', 'servicio__nombre')
    list_filter = ('estado', 'fecha', 'recordatorio_enviado')


@admin.register(HistorialReserva)
class HistorialReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'reserva', 'cambio_estado', 'fecha_cambio')
    list_filter = ('cambio_estado',)
