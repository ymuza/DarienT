from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from tu_credito.permissions import IsStaffOrReadOnly
from .models import Credito
from .serializers import CreditoSerializer


class CreditoViewSet(ModelViewSet):
    queryset = Credito.objects.select_related("cliente", "banco").all()
    serializer_class = CreditoSerializer
    permission_classes = [IsStaffOrReadOnly]

    filterset_fields = ["tipo_credito", "banco"]
    search_fields = ["descripcion", "cliente__nombre_completo"]

