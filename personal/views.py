from rest_framework.viewsets import ModelViewSet
from .models import Atendente
from .serializers import AtendenteSerializer


class AtendenteViewSet(ModelViewSet):
    queryset = Atendente.objects.all()
    serializer_class = AtendenteSerializer
