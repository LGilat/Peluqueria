from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    preferencias = models.TextField(blank=True)
    gasto_acumulado = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.nombre


class ClienteServicio(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='historial_servicios', on_delete=models.CASCADE)
    servicio = models.ForeignKey('inventario.Servicio', on_delete=models.PROTECT)
    reserva = models.OneToOneField('reservas.Reserva', on_delete=models.SET_NULL, blank=True, null=True)
    atendente = models.ForeignKey('personal.Atendente', on_delete=models.SET_NULL, blank=True, null=True)
    fecha = models.DateField()
    hora = models.TimeField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Historial de Servicios'
        ordering = ['-fecha', '-hora']

    def __str__(self):
        return f"{self.cliente.nombre} - {self.servicio.nombre} ({self.fecha})"
