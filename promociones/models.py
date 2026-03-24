from django.db import models


class Promocion(models.Model):
    nombre = models.CharField(max_length=100)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_descuento = models.CharField(max_length=50, choices=[('porcentaje', 'Porcentaje'), ('fijo', 'Fijo')])
    vigencia = models.DateField()

    def __str__(self):
        return self.nombre
