from rest_framework.viewsets import ModelViewSet
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


class NominaItemViewSet(ModelViewSet):
    queryset = NominaItem.objects.all()
    serializer_class = NominaItemSerializer


class AvisoViewSet(ModelViewSet):
    queryset = Aviso.objects.all()
    serializer_class = AvisoSerializer


class AvisoDestinatarioViewSet(ModelViewSet):
    queryset = AvisoDestinatario.objects.all()
    serializer_class = AvisoDestinatarioSerializer
