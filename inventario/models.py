from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_minutos = models.PositiveIntegerField(default=30)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre


class Stock(models.Model):
    producto = models.ForeignKey(Producto, related_name='stocks', on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    proveedor = models.ForeignKey(Proveedor, related_name='stocks', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.producto.nombre} - Cantidad: {self.cantidad}"
