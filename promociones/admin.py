from django.contrib import admin
from .models import Promocion


@admin.register(Promocion)
class PromocionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo_descuento', 'descuento', 'vigencia')
    search_fields = ('nombre',)
    list_filter = ('tipo_descuento', 'vigencia')
