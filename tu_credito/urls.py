from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bancos.views import BancoViewSet
from clientes.views import ClienteViewSet
from creditos.views import CreditoViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

router = DefaultRouter()
router.register(r"bancos", BancoViewSet)
router.register(r"clientes", ClienteViewSet)
router.register(r"creditos", CreditoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),

    # JWT
    path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    path("backoffice/bancos/", include("bancos.urls_web")),
    path("backoffice/clientes/", include("clientes.urls_web")),
    path("backoffice/creditos/", include("creditos.urls_web")),



]
