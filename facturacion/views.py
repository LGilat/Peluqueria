from django.db.models import Sum
from django.db.models.functions import ExtractMonth, ExtractYear
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Factura, LineaFactura, Ingreso, Gasto
from .serializers import FacturaSerializer, LineaFacturaSerializer, IngresoSerializer, GastoSerializer


class FacturaViewSet(ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer


class LineaFacturaViewSet(ModelViewSet):
    queryset = LineaFactura.objects.all()
    serializer_class = LineaFacturaSerializer


class IngresoViewSet(ModelViewSet):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer


class GastoViewSet(ModelViewSet):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer


class FinancialReportView(APIView):
    def get(self, request):
        year = request.query_params.get('year')

        ingresos_qs = Ingreso.objects.all()
        gastos_qs = Gasto.objects.all()

        if year:
            ingresos_qs = ingresos_qs.filter(fecha__year=year)
            gastos_qs = gastos_qs.filter(fecha__year=year)

        ingresos = (
            ingresos_qs.annotate(year=ExtractYear('fecha'), month=ExtractMonth('fecha'))
            .values('year', 'month')
            .annotate(total=Sum('cantidad'))
        )

        gastos = (
            gastos_qs.annotate(year=ExtractYear('fecha'), month=ExtractMonth('fecha'))
            .values('year', 'month')
            .annotate(total=Sum('cantidad'))
        )

        ingresos_map = {(i['year'], i['month']): i['total'] for i in ingresos}
        gastos_map = {(g['year'], g['month']): g['total'] for g in gastos}

        months = sorted(set(ingresos_map.keys()) | set(gastos_map.keys()))
        data = []
        for y, m in months:
            inc = ingresos_map.get((y, m), 0) or 0
            exp = gastos_map.get((y, m), 0) or 0
            data.append({
                'year': y,
                'month': m,
                'ingresos': inc,
                'gastos': exp,
                'margen': inc - exp,
            })

        return Response({
            'year': year,
            'data': data,
        })
