from decimal import Decimal
from django.db import models


def default_work_days():
    return ["L", "M", "X", "J", "V"]


class Atendente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    especialidad = models.CharField(max_length=100)
    contacto = models.CharField(max_length=15)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)
    dias_laborales = models.JSONField(default=default_work_days, blank=True)
    comision_porcentaje = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal("0.00"))
    comision_fija = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    servicios = models.ManyToManyField('inventario.Servicio', blank=True, related_name='atendentes')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class NominaMensual(models.Model):
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('pagada', 'Pagada'),
    )

    atendente = models.ForeignKey(Atendente, on_delete=models.CASCADE, related_name='nominas')
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    salario_base = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    comision_fija_total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    comision_porcentaje_total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    otros = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    deducciones = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    retencion_irpf = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    seguridad_social = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    total_neto = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_pago = models.DateField(blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('atendente', 'year', 'month')
        ordering = ['-year', '-month', 'atendente__apellido']

    def save(self, *args, **kwargs):
        self.total = (
            (self.salario_base or Decimal("0.00"))
            + (self.comision_fija_total or Decimal("0.00"))
            + (self.comision_porcentaje_total or Decimal("0.00"))
            + (self.otros or Decimal("0.00"))
        )
        self.total_neto = (
            self.total
            - (self.deducciones or Decimal("0.00"))
            - (self.retencion_irpf or Decimal("0.00"))
            - (self.seguridad_social or Decimal("0.00"))
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Nomina {self.month}/{self.year} - {self.atendente}"


class NominaItem(models.Model):
    nomina = models.ForeignKey(NominaMensual, on_delete=models.CASCADE, related_name='items')
    reserva = models.ForeignKey('reservas.Reserva', on_delete=models.SET_NULL, blank=True, null=True)
    concepto = models.CharField(max_length=200)
    importe = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.concepto} ({self.importe})"


class Aviso(models.Model):
    titulo = models.CharField(max_length=200)
    mensaje = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class AvisoDestinatario(models.Model):
    aviso = models.ForeignKey(Aviso, on_delete=models.CASCADE, related_name='destinatarios')
    atendente = models.ForeignKey(Atendente, on_delete=models.CASCADE, related_name='avisos')
    leido = models.BooleanField(default=False)
    leido_en = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ('aviso', 'atendente')

    def __str__(self):
        return f"{self.aviso} -> {self.atendente}"
