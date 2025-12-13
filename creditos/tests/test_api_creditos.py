import pytest
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


def test_no_autenticado_no_puede_crear_credito():
    client = APIClient()

    response = client.post("/api/creditos/", {
        "descripcion": "Crédito",
        "pago_minimo": 1000,
        "pago_maximo": 2000,
        "plazo_meses": 12,
        "tipo_credito": "AUTOMOTRIZ",
    })

    assert response.status_code == 401 or response.status_code == 403


