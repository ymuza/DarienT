from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Credito
from .serializers import CreditoSerializer


class CreditoViewSet(ModelViewSet):
    queryset = Credito.objects.select_related("cliente", "banco").all()
    serializer_class = CreditoSerializer
