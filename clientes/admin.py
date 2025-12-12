from django.contrib import admin
from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_completo",
        "email",
        "tipo_persona",
        "banco",
    )
    search_fields = (
        "nombre_completo",
        "email",
    )
    list_filter = (
        "tipo_persona",
        "banco",
    )
    raw_id_fields = ("banco",)
