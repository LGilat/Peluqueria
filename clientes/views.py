from rest_framework.viewsets import ModelViewSet
from .models import Cliente, ClienteServicio
from .serializers import ClienteSerializer, ClienteServicioSerializer


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ClienteServicioViewSet(ModelViewSet):
    queryset = ClienteServicio.objects.all()
    serializer_class = ClienteServicioSerializer
