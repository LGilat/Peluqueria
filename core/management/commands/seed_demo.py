from datetime import timedelta, time
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
            ("Aceite Capilar", "Brillo y suavidad", "9.90"),
            ("Laca Fijación", "Fijación extra", "7.50"),
            ("Tinte 6.0", "Castaño oscuro", "14.00"),
            ("Cera Modeladora", "Acabado mate", "8.20"),
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
            ("Peinado", "Peinado evento", "20.00", 40),
            ("Barba", "Perfilado y arreglo", "12.00", 20),
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
            ("Sofía", "Pérez", "sofia@example.com", "600333334", "Tratamientos", "600333335"),
            ("Carlos", "Díaz", "carlos@example.com", "600444445", "Peinados", "600444446"),
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
            ("Lucía", "Martín", "lucia@example.com", "600555555", "Calle 3", "Corte cada 3 semanas"),
            ("David", "Gómez", "david@example.com", "600666666", "Calle 4", "Tratamiento hidratante"),
            ("Marta", "Sánchez", "marta@example.com", "600777777", "Calle 5", "Peinados"),
            ("Jorge", "Navarro", "jorge@example.com", "600888888", "Calle 6", "Barba"),
            ("Paula", "Iglesias", "paula@example.com", "600999999", "Calle 7", "Color y peinado"),
            ("Hugo", "Torres", "hugo@example.com", "601111111", "Calle 8", "Corte corto"),
            ("Elena", "Romero", "elena@example.com", "601222222", "Calle 9", "Tratamientos"),
            ("Sergio", "Molina", "sergio@example.com", "601333333", "Calle 10", "Barba y corte"),
            ("Clara", "Vega", "clara@example.com", "601444444", "Calle 11", "Preferencias suaves"),
            ("Raúl", "Ortega", "raul@example.com", "601555555", "Calle 12", "Peinado"),
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
        horarios = [time(9, 0), time(10, 0), time(11, 0), time(12, 0), time(16, 0), time(17, 0), time(18, 0)]
        day_offsets = list(range(1, 8))

        created = 0
        for i, day_offset in enumerate(day_offsets):
            fecha = (now + timedelta(days=day_offset)).date()
            for j, atendente in enumerate(atendentes):
                hora = horarios[(i + j) % len(horarios)]
                cliente = clientes[(i * len(atendentes) + j) % len(clientes)]
                servicio = servicios[(i + j) % len(servicios)]

                _, was_created = Reserva.objects.get_or_create(
                    cliente=cliente,
                    servicio=servicio,
                    atendente=atendente,
                    fecha=fecha,
                    hora=hora,
                    defaults={"estado": "pendiente", "observaciones": "Demo"},
                )
                if was_created:
                    created += 1

        self.stdout.write(self.style.SUCCESS(f"Datos de ejemplo creados/actualizados. Reservas nuevas: {created}"))
