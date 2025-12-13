from django import forms
from .models import Banco


class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = ["nombre", "tipo", "direccion"]
