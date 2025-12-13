from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)


    if isinstance(exc, IntegrityError): # esto es para cachear errores de base de datos
        return Response(
            {
                "detail": "Error de integridad en la base de datos.",
                "error": str(exc),
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    if response is not None:
        return response


    return Response(
        {
            "detail": "Error interno del servidor.",
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
