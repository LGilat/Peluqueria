from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Cliente
from .serializers import ClienteSerializer


class ClienteList(ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ClienteDetail(RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
