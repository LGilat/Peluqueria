from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Atendente
from .serializers import AtendenteSerializer


class AtendenteList(ListCreateAPIView):
    queryset = Atendente.objects.all()
    serializer_class = AtendenteSerializer


class AtendenteDetail(RetrieveUpdateDestroyAPIView):
    queryset = Atendente.objects.all()
    serializer_class = AtendenteSerializer
