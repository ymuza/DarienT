
from rest_framework.viewsets import ModelViewSet
from bancos.models import Banco
from .serializers import BancoSerializer


class BancoViewSet(ModelViewSet):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer

    filterset_fields = ["tipo"]
    search_fields = ["nombre"]