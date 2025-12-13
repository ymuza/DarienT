"""
Django settings for tu_credito project.
"""
from datetime import timedelta
from pathlib import Path

import environ
import rest_framework.filters

# ======================
# BASE DIR
# ======================
BASE_DIR = Path(__file__).resolve().parent.parent

# ======================
# ENV
# ======================
env = environ.Env(
    DEBUG=(bool, False),
)

# Carga automática del .env (más robusta)
environ.Env.read_env(BASE_DIR / ".env")

# print("=" * 50)
# print(f"BASE_DIR: {BASE_DIR}")
# print(f".env path: {BASE_DIR / '.env'}")
# print(f".env exists: {(BASE_DIR / '.env').exists()}")
# print(f"DB_USER from env: {env('DB_USER', default='NOT_FOUND')}")
# print(f"DB_PASSWORD from env: {env('DB_PASSWORD', default='NOT_FOUND')}")
# print("=" * 50)
# ======================
# CORE SETTINGS
# ======================
SECRET_KEY = env("SECRET_KEY", default="unsafe-dev-key")
DEBUG = env("DEBUG", default=True)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["127.0.0.1", "localhost"])

# ======================
# APPLICATIONS
# ======================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "drf_spectacular",
    "django_filters",

    "bancos",
    "clientes",
    "creditos",
]

# ===========================
# CONFIGURACION DE PAGINACIÓN
# ===========================

REST_FRAMEWORK = {

    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",

    "DEFAULT_AUTHENTICATION_CLASSES": (  # con esto todaas llas clases tienen auth
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),

    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",

    "PAGE_SIZE": 10,

    "EXCEPTION_HANDLER": "tu_credito.exceptions.custom_exception_handler",

    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",
                                "rest_framework.filters.SearchFilter"),
}


SPECTACULAR_SETTINGS = {
    "TITLE": "Tu Crédito API",
    "DESCRIPTION": "API para gestión de Bancos, Clientes y Créditos",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,

    # JWT support
    "SECURITY": [{"bearerAuth": []}],
    "COMPONENT_SPLIT_REQUEST": True,
}

# ======================
# AUTENTICACIÓN CON JWT
# ======================


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# ======================
# MIDDLEWARE
# ======================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "tu_credito.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

TEMPLATES[0]["DIRS"] = [BASE_DIR / "templates"]



WSGI_APPLICATION = "tu_credito.wsgi.application"

# ======================
# DATABASE (ROBUSTA)
# ======================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME", default="tu_credito"),
        "USER": env("DB_USER", default="postgres"),
        "PASSWORD": env("DB_PASSWORD", default="postgres"),
        "HOST": env("DB_HOST", default="127.0.0.1"),
        "PORT": env("DB_PORT", default="5432"),
    }
}

# ======================
# PASSWORD VALIDATION
# ======================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ======================
# I18N
# ======================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ======================
# STATIC
# ======================
STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
