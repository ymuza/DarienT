from django.contrib import admin

# Register your models here.
from .models import Banco


@admin.register(Banco)
class BancoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo")
    search_fields = ("nombre",)
    list_filter = ("tipo",)

