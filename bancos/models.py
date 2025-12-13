from django.db import models

# Create your models here.
from django.db import models


class Banco(models.Model):
    class Tipo(models.TextChoices):
        PRIVADO = "PRIVADO", "Privado"
        GOBIERNO = "GOBIERNO", "Gobierno"

    nombre = models.CharField(max_length=150)
    tipo = models.CharField(max_length=20, choices=Tipo.choices)
    direccion = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Banco"
        verbose_name_plural = "Bancos"

    def __str__(self) -> str:
        return self.nombre
