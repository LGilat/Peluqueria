from django.db import models


class Atendente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    especialidad = models.CharField(max_length=100)
    contacto = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
