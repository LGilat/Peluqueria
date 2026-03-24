from django.db import models
from django.utils import timezone


ESTADOS_RESERVA = [
    ('pendiente', 'Pendiente'),
    ('realizada', 'Realizada'),
    ('cancelada', 'Cancelada'),
    ('finalizada', 'Finalizada')
]


class Reserva(models.Model):
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    servicio = models.ForeignKey('inventario.Servicio', on_delete=models.PROTECT)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=50, choices=ESTADOS_RESERVA)
    observaciones = models.TextField(blank=True)
    cancelado_en = models.DateTimeField(blank=True, null=True)
    motivo_cancelacion = models.TextField(blank=True)
    recordatorio_enviado = models.BooleanField(default=False)
    creado_en = models.DateTimeField(default=timezone.now, editable=False)
    actualizado_en = models.DateTimeField(auto_now=True)
    atendente = models.ForeignKey(
        'personal.Atendente',
        related_name='reservas',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Reserva #{self.id} para {self.cliente.nombre} - Servicio: {self.servicio}"

    class Meta:
        verbose_name_plural = 'Reservas'


class HistorialReserva(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    cambio_estado = models.CharField(max_length=100)
    fecha_cambio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"Historial de Reserva #{self.reserva.id} para "
            f"{self.reserva.cliente.nombre} - Servicio: {self.reserva.servicio}"
        )

    class Meta:
        verbose_name_plural = 'Historial de Reservas'
