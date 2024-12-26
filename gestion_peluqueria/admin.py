from django.contrib import admin
from .models import Cliente, Producto, Proveedor, Stock, Reserva, HistorialReserva, Atendente, Factura, LineaFactura, Ingreso, Gasto, Promocion

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Stock)
admin.site.register(Reserva)
admin.site.register(HistorialReserva)
admin.site.register(Atendente)
admin.site.register(Factura)
admin.site.register(LineaFactura)
admin.site.register(Ingreso)
admin.site.register(Gasto)
admin.site.register(Promocion)
