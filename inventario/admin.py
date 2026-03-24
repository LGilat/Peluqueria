from django.contrib import admin
from .models import Producto, Proveedor, Stock, Servicio


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio')
    search_fields = ('nombre',)


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'duracion_minutos', 'activo')
    search_fields = ('nombre',)
    list_filter = ('activo',)


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'telefono')
    search_fields = ('nombre', 'email')


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'proveedor', 'cantidad')
    search_fields = ('producto__nombre', 'proveedor__nombre')
    list_filter = ('proveedor',)
