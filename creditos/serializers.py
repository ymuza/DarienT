from rest_framework import serializers
from .models import Credito


class CreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credito
        fields = "__all__"

    def validate(self, data):
        pago_minimo = data.get("pago_minimo")
        pago_maximo = data.get("pago_maximo")
        cliente = data.get("cliente")
        banco = data.get("banco")
        plazo = data.get("plazo_meses")

        # 1️⃣ Validación financiera
        if pago_minimo and pago_maximo and pago_minimo > pago_maximo:
            raise serializers.ValidationError(
                {"pago_minimo": "El pago mínimo no puede ser mayor al pago máximo."}
            )

        # 2️⃣ Validación de plazo
        if plazo is not None and plazo <= 0:
            raise serializers.ValidationError(
                {"plazo_meses": "El plazo debe ser mayor a 0 meses."}
            )

        # 3️⃣ Validación de coherencia Cliente ↔ Banco
        if cliente and banco:
            if cliente.banco_id != banco.id:
                raise serializers.ValidationError(
                    {
                        "banco": (
                            "El banco del crédito debe coincidir "
                            "con el banco del cliente."
                        )
                    }
                )

        return data
