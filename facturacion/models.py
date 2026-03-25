from django.db import models
from django.utils import timezone


class Factura(models.Model):
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    impuestos = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    promocion = models.ForeignKey('promociones.Promocion', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"Factura #{self.id} para {self.cliente.nombre}"

    class Meta:
        verbose_name_plural = 'Facturas'


class LineaFactura(models.Model):
    factura = models.ForeignKey(Factura, related_name='lineas_factura', on_delete=models.CASCADE)
    producto = models.ForeignKey('inventario.Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Linea de Factura #{self.factura.id} - Producto: {self.producto.nombre}"

    class Meta:
        verbose_name_plural = 'Lineas de Factura'


class Ingreso(models.Model):
    tipo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100, default='Otros')
    subcategoria = models.CharField(max_length=100, blank=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(default=timezone.now)
    iva_incluido = models.BooleanField(default=True)
    iva_porcentaje = models.DecimalField(max_digits=5, decimal_places=2, default=21.00)

    def __str__(self):
        return f"Ingreso #{self.id} de tipo {self.tipo}"

    class Meta:
        verbose_name_plural = 'Ingresos'


class Gasto(models.Model):
    tipo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100, default='Varios')
    subcategoria = models.CharField(max_length=100, blank=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(default=timezone.now)
    proveedor = models.ForeignKey('inventario.Proveedor', on_delete=models.SET_NULL, blank=True, null=True)
    iva_incluido = models.BooleanField(default=True)
    iva_porcentaje = models.DecimalField(max_digits=5, decimal_places=2, default=21.00)

    def __str__(self):
        return f"Gasto #{self.id} de tipo {self.tipo}"

    class Meta:
        verbose_name_plural = 'Gastos'
