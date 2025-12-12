from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator
from bancos.models import Banco
from clientes.models import Cliente


class Credito(models.Model):
    class TipoCredito(models.TextChoices):
        AUTOMOTRIZ = "AUTOMOTRIZ", "Automotriz"
        HIPOTECARIO = "HIPOTECARIO", "Hipotecario"
        COMERCIAL = "COMERCIAL", "Comercial"

    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="creditos"
    )
    descripcion = models.CharField(max_length=255)
    pago_minimo = models.DecimalField(
        max_digits=12, decimal_places=2, validators=[MinValueValidator(0)]
    )
    pago_maximo = models.DecimalField(
        max_digits=12, decimal_places=2, validators=[MinValueValidator(0)]
    )
    plazo_meses = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    fecha_registro = models.DateTimeField(auto_now_add=True)
    banco = models.ForeignKey(
        Banco, on_delete=models.PROTECT, related_name="creditos"
    )
    tipo_credito = models.CharField(max_length=20, choices=TipoCredito.choices)

    class Meta:
        verbose_name = "Crédito"
        verbose_name_plural = "Créditos"

    def __str__(self) -> str:
        return f"{self.cliente} - {self.tipo_credito}"
