import pytest
from creditos.models import Credito
from clientes.models import Cliente
from bancos.models import Banco
from datetime import date
from django.core.exceptions import ValidationError

pytestmark = pytest.mark.django_db


def test_pago_minimo_no_puede_ser_mayor_al_maximo():
    banco = Banco.objects.create(nombre="Banco Test", tipo="PRIVADO")
    cliente = Cliente.objects.create(
        dni="11111111",
        nombre_completo="Juan Perez",
        fecha_nacimiento=date(1990, 1, 1),
        edad=34,
        email="juan@test.com",
        tipo_persona="NATURAL",
        banco=banco,
    )

    credito = Credito(
        cliente=cliente,
        banco=banco,
        descripcion="Crédito inválido",
        pago_minimo=3000,
        pago_maximo=1000,
        plazo_meses=12,
        tipo_credito="AUTOMOTRIZ",
    )

    with pytest.raises(ValidationError):
        credito.full_clean()



def test_banco_credito_debe_coincidir_con_banco_cliente():
    banco_cliente = Banco.objects.create(nombre="Banco A", tipo="PRIVADO")
    banco_credito = Banco.objects.create(nombre="Banco B", tipo="PRIVADO")

    cliente = Cliente.objects.create(
        dni="22222222",
        nombre_completo="Ana Lopez",
        fecha_nacimiento=date(1990, 1, 1),
        edad=34,
        email="ana@test.com",
        tipo_persona="NATURAL",
        banco=banco_cliente,
    )

    credito = Credito(
        cliente=cliente,
        banco=banco_credito,
        descripcion="Crédito inconsistente",
        pago_minimo=1000,
        pago_maximo=2000,
        plazo_meses=12,
        tipo_credito="HIPOTECARIO",
    )

    with pytest.raises(ValidationError):
        credito.full_clean()
