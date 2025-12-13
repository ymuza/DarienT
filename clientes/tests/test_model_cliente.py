import pytest
from clientes.models import Cliente
from bancos.models import Banco
from django.db import IntegrityError
from datetime import date

pytestmark = pytest.mark.django_db


def test_no_permite_dni_duplicado():
    banco = Banco.objects.create(
        nombre="Banco Test",
        tipo="PRIVADO"
    )

    Cliente.objects.create(
        dni="12345678",
        nombre_completo="Juan Perez",
        fecha_nacimiento=date(1990, 1, 1),
        edad=34,
        email="juan@test.com",
        tipo_persona="NATURAL",
        banco=banco,
    )

    with pytest.raises(IntegrityError):
        Cliente.objects.create(
            dni="12345678",
            nombre_completo="Otro",
            fecha_nacimiento=date(1995, 1, 1),
            edad=29,
            email="otro@test.com",
            tipo_persona="NATURAL",
            banco=banco,
        )
