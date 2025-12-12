from rest_framework import serializers
from datetime import date
from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

    def validate_dni(self, value):
        qs = Cliente.objects.filter(dni=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError("Ya existe un cliente con ese DNI.")

        return value


    def validate(self, data):
        """Valida que la edad coincida con la fecha de nacimiento."""
        fecha_nacimiento = data.get("fecha_nacimiento")
        edad = data.get("edad")

        if fecha_nacimiento and edad:
            today = date.today()
            calculated_age = today.year - fecha_nacimiento.year - (
                (today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day)
            )
            if calculated_age != edad:
                raise serializers.ValidationError(
                    "La edad no coincide con la fecha de nacimiento."
                )
        return data
