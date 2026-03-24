from django.contrib import admin
from .models import Factura, LineaFactura, Ingreso, Gasto


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'subtotal', 'impuestos', 'total', 'fecha')
    search_fields = ('cliente__nombre', 'cliente__apellido')
    list_filter = ('fecha',)


@admin.register(LineaFactura)
class LineaFacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'factura', 'producto', 'cantidad', 'precio_unitario')
    search_fields = ('producto__nombre',)


@admin.register(Ingreso)
class IngresoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'cantidad', 'fecha')
    list_filter = ('tipo',)


@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'cantidad', 'fecha', 'proveedor')
    list_filter = ('tipo',)
