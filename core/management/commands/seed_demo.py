from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone

from clientes.models import Cliente
from personal.models import Atendente
from inventario.models import Servicio, Producto, Proveedor, Stock
from reservas.models import Reserva


class Command(BaseCommand):
    help = "Crea datos de ejemplo para desarrollo"

    def handle(self, *args, **options):
        self.stdout.write("Creando datos de ejemplo...")

        proveedor, _ = Proveedor.objects.get_or_create(
            nombre="Proveedor Demo",
            defaults={
                "email": "proveedor@example.com",
                "telefono": "600123123",
                "direccion": "Calle Proveedor 123",
            },
        )

        productos = [
            ("Champú Profesional", "Champú nutritivo", "12.50"),
            ("Mascarilla Reparadora", "Mascarilla intensa", "18.00"),
        ]
        for nombre, descripcion, precio in productos:
            producto, _ = Producto.objects.get_or_create(
                nombre=nombre,
                defaults={"descripcion": descripcion, "precio": precio},
            )
            Stock.objects.get_or_create(
                producto=producto,
                proveedor=proveedor,
                defaults={"cantidad": 25},
            )

        servicios_data = [
            ("Corte", "Corte de cabello", "15.00", 30),
            ("Color", "Tinte completo", "35.00", 60),
            ("Tratamiento", "Tratamiento nutritivo", "25.00", 45),
        ]
        servicios = []
        for nombre, descripcion, precio, duracion in servicios_data:
            servicio, _ = Servicio.objects.get_or_create(
                nombre=nombre,
                defaults={
                    "descripcion": descripcion,
                    "precio": precio,
                    "duracion_minutos": duracion,
                    "activo": True,
                },
            )
            servicios.append(servicio)

        atendentes_data = [
            ("Laura", "García", "laura@example.com", "600111111", "Color", "600111112"),
            ("Miguel", "Santos", "miguel@example.com", "600222222", "Corte", "600222223"),
        ]
        atendentes = []
        for nombre, apellido, email, telefono, especialidad, contacto in atendentes_data:
            atendente, _ = Atendente.objects.get_or_create(
                email=email,
                defaults={
                    "nombre": nombre,
                    "apellido": apellido,
                    "telefono": telefono,
                    "especialidad": especialidad,
                    "contacto": contacto,
                },
            )
            atendentes.append(atendente)

        clientes_data = [
            ("Ana", "López", "ana@example.com", "600333333", "Calle 1", "Prefiere mañanas"),
            ("Pedro", "Ruiz", "pedro@example.com", "600444444", "Calle 2", "Color sin amoniaco"),
        ]
        clientes = []
        for nombre, apellido, email, telefono, direccion, preferencias in clientes_data:
            cliente, _ = Cliente.objects.get_or_create(
                email=email,
                defaults={
                    "nombre": nombre,
                    "apellido": apellido,
                    "telefono": telefono,
                    "direccion": direccion,
                    "preferencias": preferencias,
                },
            )
            clientes.append(cliente)

        now = timezone.localtime()
        for i, cliente in enumerate(clientes):
            Reserva.objects.get_or_create(
                cliente=cliente,
                servicio=servicios[i % len(servicios)],
                atendente=atendentes[i % len(atendentes)],
                fecha=(now + timedelta(days=1 + i)).date(),
                hora=(now + timedelta(hours=2 + i)).time().replace(second=0, microsecond=0),
                defaults={"estado": "pendiente", "observaciones": "Demo"},
            )

        self.stdout.write(self.style.SUCCESS("Datos de ejemplo creados/actualizados."))
