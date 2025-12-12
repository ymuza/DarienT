from django.shortcuts import render
from psycopg import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Cliente
from .serializers import ClienteSerializer


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.select_related("banco").all()
    serializer_class = ClienteSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response({"detail": "Ya existe un cliente con ese DNI."},
                            status=status.HTTP_400_BAD_REQUEST, )

    filterset_fields = ["tipo_persona", "banco"]
    search_fields = ["nombre_completo", "email"]
