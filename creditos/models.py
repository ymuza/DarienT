from django.db import models
from django.core.exceptions import ValidationError

class Credito(models.Model):
    cliente = models.ForeignKey(
        "clientes.Cliente",
        on_delete=models.CASCADE,
        related_name="creditos",
    )
    banco = models.ForeignKey(
        "bancos.Banco",
        on_delete=models.PROTECT,
        related_name="creditos",
    )
    descripcion = models.CharField(max_length=255)
    pago_minimo = models.DecimalField(max_digits=10, decimal_places=2)
    pago_maximo = models.DecimalField(max_digits=10, decimal_places=2)
    plazo_meses = models.PositiveIntegerField()
    tipo_credito = models.CharField(
        max_length=20,
        choices=[
            ("AUTOMOTRIZ", "Automotriz"),
            ("HIPOTECARIO", "Hipotecario"),
            ("COMERCIAL", "Comercial"),
        ],
    )
    fecha_registro = models.DateTimeField(auto_now_add=True)


    def clean(self):

        if self.pago_minimo > self.pago_maximo:
            raise ValidationError(
                {"pago_minimo": "El pago mínimo no puede ser mayor al pago máximo."}
            )

        if self.cliente and self.banco:
            if self.cliente.banco_id != self.banco_id:
                raise ValidationError(
                    {
                        "banco": (
                            "El banco del crédito debe coincidir "
                            "con el banco del cliente."
                        )
                    }
                )


    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
