from django import forms
from .models import Credito


class CreditoForm(forms.ModelForm):
    class Meta:
        model = Credito
        fields = [
            "cliente",
            "banco",
            "descripcion",
            "pago_minimo",
            "pago_maximo",
            "plazo_meses",
            "tipo_credito",
        ]
