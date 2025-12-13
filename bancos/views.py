from django.db.models import ProtectedError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from bancos.models import Banco
from tu_credito.permissions import IsStaffOrReadOnly
from .serializers import BancoSerializer


class BancoViewSet(ModelViewSet):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer

    permission_classes = [IsStaffOrReadOnly]
    filterset_fields = ["tipo"]
    search_fields = ["nombre"]

    def destroy(self, request, *args, **kwargs):
        banco = self.get_object()

        try:
            banco.delete()
        except ProtectedError:
            return Response(
                {
                    "detail": "No se puede eliminar el banco porque tiene clientes o créditos asociados."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(status=status.HTTP_204_NO_CONTENT)
