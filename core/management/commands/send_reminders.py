from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone

from reservas.models import Reserva


class Command(BaseCommand):
    help = "Marca recordatorios enviados para reservas de manana (placeholder)"

    def handle(self, *args, **options):
        now = timezone.localtime()
        target_date = (now + timedelta(days=1)).date()

        pendientes = Reserva.objects.filter(
            fecha=target_date,
            estado__in=['pendiente', 'realizada'],
            recordatorio_enviado=False,
        )

        count = pendientes.update(recordatorio_enviado=True)
        self.stdout.write(self.style.SUCCESS(f"Recordatorios marcados: {count}"))
