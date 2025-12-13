from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from bancos.models import Banco


class Cliente(models.Model):
    class TipoPersona(models.TextChoices):
        NATURAL = "NATURAL", "Natural"
        JURIDICO = "JURIDICO", "Jurídico"

    dni = models.CharField(max_length=9, unique=True,  help_text="Documento Nacional de Identidad")
    nombre_completo = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    edad = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)]
    )
    nacionalidad = models.CharField(max_length=80, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=30, blank=True)
    tipo_persona = models.CharField(max_length=20, choices=TipoPersona.choices)
    banco = models.ForeignKey(
        Banco, on_delete=models.PROTECT, related_name="clientes"
    )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self) -> str:
        return f"{self.nombre_completo},({self.dni})"