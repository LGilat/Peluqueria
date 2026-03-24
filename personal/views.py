from datetime import date
from decimal import Decimal

from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Sum
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from reservas.models import Reserva
from .models import Atendente, NominaMensual, NominaItem, Aviso, AvisoDestinatario
from .serializers import (
    AtendenteSerializer,
    NominaMensualSerializer,
    NominaItemSerializer,
    AvisoSerializer,
    AvisoDestinatarioSerializer,
)


class AtendenteViewSet(ModelViewSet):
    queryset = Atendente.objects.all()
    serializer_class = AtendenteSerializer


class NominaMensualViewSet(ModelViewSet):
    queryset = NominaMensual.objects.all()
    serializer_class = NominaMensualSerializer

    @action(detail=False, methods=['post'])
    def recalcular(self, request):
        year = int(request.data.get('year', date.today().year))
        month = int(request.data.get('month', date.today().month))
        atendente_id = request.data.get('atendente')

        reservas = Reserva.objects.filter(
            fecha__year=year,
            fecha__month=month,
            estado__in=['realizada', 'finalizada'],
        ).select_related('servicio', 'atendente', 'cliente')

        if atendente_id:
            reservas = reservas.filter(atendente_id=atendente_id)

        resultado = []
        for atendente in Atendente.objects.all():
            if atendente_id and str(atendente.id) != str(atendente_id):
                continue

            atendente_reservas = reservas.filter(atendente_id=atendente.id)
            total_servicios = atendente_reservas.count()
            base = Decimal('0.00')
            comision_fija = (atendente.comision_fija or Decimal('0.00')) * total_servicios
            porcentaje = atendente.comision_porcentaje or Decimal('0.00')

            total_servicios_importe = Decimal('0.00')
            for r in atendente_reservas:
                total_servicios_importe += r.servicio.precio

            comision_porcentaje = (total_servicios_importe * porcentaje) / Decimal('100.00')

            nomina, _ = NominaMensual.objects.get_or_create(
                atendente=atendente,
                year=year,
                month=month,
                defaults={
                    'salario_base': base,
                    'comision_fija_total': comision_fija,
                    'comision_porcentaje_total': comision_porcentaje,
                    'otros': Decimal('0.00'),
                }
            )

            nomina.comision_fija_total = comision_fija
            nomina.comision_porcentaje_total = comision_porcentaje
            nomina.save()

            resultado.append({
                'atendente': atendente.id,
                'total_servicios': total_servicios,
                'comision_fija_total': str(comision_fija),
                'comision_porcentaje_total': str(comision_porcentaje),
            })

        return Response({'year': year, 'month': month, 'resultado': resultado})


class NominaItemViewSet(ModelViewSet):
    queryset = NominaItem.objects.all()
    serializer_class = NominaItemSerializer


class AvisoViewSet(ModelViewSet):
    queryset = Aviso.objects.all()
    serializer_class = AvisoSerializer

    @action(detail=False, methods=['post'])
    def enviar_email(self, request):
        aviso_id = request.data.get('aviso')
        if not aviso_id:
            return Response({'detail': 'aviso requerido'}, status=400)

        destinatarios = AvisoDestinatario.objects.filter(aviso_id=aviso_id).select_related('aviso', 'atendente')
        enviados = 0
        for item in destinatarios:
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

        return Response({'enviados': enviados})


class AvisoDestinatarioViewSet(ModelViewSet):
    queryset = AvisoDestinatario.objects.all()
    serializer_class = AvisoDestinatarioSerializer
