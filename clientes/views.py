from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Cliente
from .serializers import ClienteSerializer


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.select_related("banco").all()
    serializer_class = ClienteSerializer

