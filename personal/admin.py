from django.contrib import admin
from .models import Atendente


@admin.register(Atendente)
class AtendenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'email', 'telefono', 'especialidad')
    search_fields = ('nombre', 'apellido', 'email', 'especialidad')
    list_filter = ('especialidad',)
