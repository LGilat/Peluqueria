from django.contrib import admin
from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'email', 'telefono', 'gasto_acumulado')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('nombre',)
