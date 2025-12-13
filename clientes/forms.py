from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            "dni",
            "nombre_completo",
            "fecha_nacimiento",
            "edad",
            "nacionalidad",
            "direccion",
            "email",
            "telefono",
            "tipo_persona",
            "banco",
        ]
