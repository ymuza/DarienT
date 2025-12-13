from rest_framework import serializers
from .models import Banco


class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = "__all__"

    def validate_nombre(self, value):
        qs = Banco.objects.filter(nombre__iexact=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError(
                "Ya existe un banco con ese nombre."
            )
        return value
