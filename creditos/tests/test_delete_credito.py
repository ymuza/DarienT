import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from bancos.models import Banco
from clientes.models import Cliente
from creditos.models import Credito
from datetime import date

pytestmark = pytest.mark.django_db


def test_se_puede_borrar_credito():
    user = User.objects.create_user(username="test", password="1234", is_staff=True)
    client = APIClient()
    client.force_authenticate(user=user)

    banco = Banco.objects.create(nombre="Banco Test", tipo="PRIVADO")
    cliente = Cliente.objects.create(
        dni="44444444",
        nombre_completo="Laura Perez",
        fecha_nacimiento=date(1990, 1, 1),
        edad=34,
        email="laura@test.com",
        tipo_persona="NATURAL",
        banco=banco,
    )

    credito = Credito.objects.create(
        cliente=cliente,
        banco=banco,
        descripcion="Crédito",
        pago_minimo=1000,
        pago_maximo=2000,
        plazo_meses=12,
        tipo_credito="COMERCIAL",
    )

    response = client.delete(f"/api/creditos/{credito.id}/")
    assert response.status_code == 204
