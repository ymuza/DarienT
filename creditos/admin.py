from django.contrib import admin
from .models import Credito


@admin.register(Credito)
class CreditoAdmin(admin.ModelAdmin):
    list_display = (
        "cliente",
        "tipo_credito",
        "banco",
        "pago_minimo",
        "pago_maximo",
        "plazo_meses",
        "fecha_registro",
    )
    search_fields = (
        "cliente__nombre_completo",
        "descripcion",
    )
    list_filter = (
        "tipo_credito",
        "banco",
    )
    raw_id_fields = ("cliente", "banco")
    ordering = ("-fecha_registro",)
