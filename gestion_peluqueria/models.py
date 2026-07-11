from django.db import models
from django.contrib.auth.models import AbstractUser


ESTADOS_RESERVA = [
    ('pendiente', 'Pendiente'),
    ('realizada', 'Realizada'),
    ('cancelada', 'Cancelada'),
    ('finalizada', 'Finalizada')
]


# Modelo de Cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


# Modelo de Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


# Modelo de Proveedor
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'


# Modelo de Stock
class Stock(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='stocks')
    cantidad = models.IntegerField(default=0)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.producto.nombre} - Cantidad: {self.cantidad}"

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'


# Modelo de Atendente
class Atendente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    especialidad = models.CharField(max_length=100)
    contacto = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = 'Atendente'
        verbose_name_plural = 'Atendentes'


# Modelo de Reserva
class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')
    servicio = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=50, choices=ESTADOS_RESERVA, default='pendiente')
    observaciones = models.TextField(blank=True, null=True)
    atendente = models.ForeignKey(Atendente, related_name='reservas', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"Reserva #{self.id} para {self.cliente.nombre} - Servicio: {self.servicio}"

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'


# Modelo de Historial de Reserva
class HistorialReserva(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='historial')
    cambio_estado = models.CharField(max_length=100)
    fecha_cambio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Historial de Reserva #{self.reserva.id} - Cambio: {self.cambio_estado}"

    class Meta:
        verbose_name = 'Historial de Reserva'
        verbose_name_plural = 'Historial de Reservas'


# Modelo de Factura
class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='facturas')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    impuestos = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    promocion = models.ForeignKey('Promocion', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"Factura #{self.id} para {self.cliente.nombre}"

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'


# Modelo de Linea de Factura
class LineaFactura(models.Model):
    factura = models.ForeignKey(Factura, related_name='lineas_factura', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Línea de Factura #{self.factura.id} - Producto: {self.producto.nombre}"

    class Meta:
        verbose_name = 'Línea de Factura'
        verbose_name_plural = 'Líneas de Factura'


# Modelo de Ingreso
class Ingreso(models.Model):
    tipo = models.CharField(max_length=100)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ingreso #{self.id} de tipo {self.tipo}"

    class Meta:
        verbose_name = 'Ingreso'
        verbose_name_plural = 'Ingresos'


# Modelo de Gasto
class Gasto(models.Model):
    tipo = models.CharField(max_length=100)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"Gasto #{self.id} de tipo {self.tipo}"

    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'


# Modelo de Promocion
class Promocion(models.Model):
    nombre = models.CharField(max_length=100)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_descuento = models.CharField(max_length=50, choices=[('porcentaje', 'Porcentaje'), ('fijo', 'Fijo')])
    vigencia = models.DateField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Promoción'
        verbose_name_plural = 'Promociones'
