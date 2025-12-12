from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bancos.views import BancoViewSet
from clientes.views import ClienteViewSet
from creditos.views import CreditoViewSet


router = DefaultRouter()
router.register(r"bancos", BancoViewSet)
router.register(r"clientes", ClienteViewSet)
router.register(r"creditos", CreditoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
