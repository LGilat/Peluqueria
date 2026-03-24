from django.apps import apps
from django.db import models
from django.db.models import F
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

    def save(self, *args, **kwargs):
        previous_estado = None
        if self.pk:
            previous = Reserva.objects.filter(pk=self.pk).only('estado', 'cancelado_en').first()
            if previous:
                previous_estado = previous.estado

        if self.estado == 'cancelada' and not self.cancelado_en:
            self.cancelado_en = timezone.now()

        if self.cancelado_en and self.estado != 'cancelada':
            self.estado = 'cancelada'

        super().save(*args, **kwargs)

        if self.estado in ('realizada', 'finalizada') and previous_estado not in ('realizada', 'finalizada'):
            ClienteServicio = apps.get_model('clientes', 'ClienteServicio')
            if not ClienteServicio.objects.filter(reserva_id=self.id).exists():
                ClienteServicio.objects.create(
                    cliente=self.cliente,
                    servicio=self.servicio,
                    reserva=self,
                    atendente=self.atendente,
                    fecha=self.fecha,
                    hora=self.hora,
                    precio=self.servicio.precio,
                )
                apps.get_model('clientes', 'Cliente').objects.filter(pk=self.cliente_id).update(
                    gasto_acumulado=F('gasto_acumulado') + self.servicio.precio
                )


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
