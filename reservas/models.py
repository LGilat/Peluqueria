from django.db import models


ESTADOS_RESERVA = [
    ('pendiente', 'Pendiente'),
    ('realizada', 'Realizada'),
    ('cancelada', 'Cancelada'),
    ('finalizada', 'Finalizada')
]


class Reserva(models.Model):
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    servicio = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=50, choices=ESTADOS_RESERVA)
    observaciones = models.TextField(blank=True)
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
