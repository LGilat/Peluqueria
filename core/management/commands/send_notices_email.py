from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings

from personal.models import AvisoDestinatario


class Command(BaseCommand):
    help = "Envia avisos por email a destinatarios"

    def handle(self, *args, **options):
        pendientes = AvisoDestinatario.objects.filter(leido=False).select_related('aviso', 'atendente')
        enviados = 0
        for item in pendientes:
            if not item.atendente.email:
                continue
            send_mail(
                item.aviso.titulo,
                item.aviso.mensaje,
                settings.DEFAULT_FROM_EMAIL,
                [item.atendente.email],
                fail_silently=True,
            )
            item.leido = True
            item.save(update_fields=['leido'])
            enviados += 1

        self.stdout.write(self.style.SUCCESS(f"Emails enviados: {enviados}"))
