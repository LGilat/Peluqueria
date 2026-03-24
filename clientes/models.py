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
