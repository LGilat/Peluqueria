from django.contrib import admin
from .models import Atendente, NominaMensual, NominaItem, Aviso, AvisoDestinatario


class NominaItemInline(admin.TabularInline):
    model = NominaItem
    extra = 0


@admin.register(Atendente)
class AtendenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'email', 'telefono', 'especialidad', 'hora_inicio', 'hora_fin')
    search_fields = ('nombre', 'apellido', 'email', 'especialidad')
    list_filter = ('especialidad',)


@admin.register(NominaMensual)
class NominaMensualAdmin(admin.ModelAdmin):
    list_display = ('id', 'atendente', 'month', 'year', 'salario_base', 'total')
    list_filter = ('year', 'month')
    inlines = [NominaItemInline]


@admin.register(NominaItem)
class NominaItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomina', 'concepto', 'importe')


@admin.register(Aviso)
class AvisoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'creado_en')


@admin.register(AvisoDestinatario)
class AvisoDestinatarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'aviso', 'atendente', 'leido', 'leido_en')
