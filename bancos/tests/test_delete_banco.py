import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from bancos.models import Banco
from clientes.models import Cliente
from django.contrib.auth.models import User

# @pytest.mark.django_db
# def test_no_se_puede_borrar_banco_con_clientes():   # DOBLE CHEQUEAR ESTE TEST
#     client = APIClient()
#
#     # Crear usuario autenticado
#     user = User.objects.create_user(
#         username="testuser",
#         password="testpass123"
#     )
#     client.force_authenticate(user=user)
#
#     # Crear banco
#     banco = Banco.objects.create(
#         nombre="Banco Test",
#         tipo="PRIVADO",
#         direccion="Calle Falsa 123"
#     )
#
#     # Crear cliente asociado
#     Cliente.objects.create(
#         dni="12345678",
#         nombre_completo="Juan Perez",
#         fecha_nacimiento="1990-01-01",
#         edad=34,
#         nacionalidad="Argentina",
#         direccion="Calle 1",
#         email="juan@test.com",
#         telefono="123456",
#         tipo_persona="NATURAL",
#         banco=banco,
#     )
#
#     url = f"/api/bancos/{banco.id}/"
#     response = client.delete(url)
#
#     assert response.status_code == status.HTTP_400_BAD_REQUEST
#     assert Banco.objects.filter(id=banco.id).exists()
import pytest
from bancos.models import Banco
from clientes.models import Cliente
from django.db.models.deletion import ProtectedError
from datetime import date

pytestmark = pytest.mark.django_db


def test_no_se_puede_borrar_banco_con_clientes():
    banco = Banco.objects.create(nombre="Banco Protegido", tipo="PRIVADO")

    Cliente.objects.create(
        dni="99999999",
        nombre_completo="Juan Perez",
        fecha_nacimiento=date(1990, 1, 1),
        edad=34,
        email="juan@test.com",
        tipo_persona="NATURAL",
        banco=banco,
    )

    with pytest.raises(ProtectedError):
        banco.delete()
