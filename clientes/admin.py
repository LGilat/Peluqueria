from django.contrib import admin
from .models import Cliente, ClienteServicio


class ClienteServicioInline(admin.TabularInline):
    model = ClienteServicio
    extra = 0


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'email', 'telefono', 'gasto_acumulado')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('nombre',)
    inlines = [ClienteServicioInline]


@admin.register(ClienteServicio)
class ClienteServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'servicio', 'fecha', 'hora', 'precio', 'atendente')
    search_fields = ('cliente__nombre', 'cliente__apellido', 'servicio__nombre')
    list_filter = ('servicio', 'fecha')
