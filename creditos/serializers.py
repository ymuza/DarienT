from rest_framework import serializers
from .models import Credito


class CreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credito
        fields = "__all__"

    def validate(self, data):
        pago_minimo = data.get("pago_minimo")
        pago_maximo = data.get("pago_maximo")

        if pago_minimo and pago_maximo and pago_minimo > pago_maximo:
            raise serializers.ValidationError(
                "El pago mínimo no puede ser mayor que el pago máximo."
            )
        return data
