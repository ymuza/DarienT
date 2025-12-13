from django.contrib.auth.decorators import login_required
from .models import Banco
from .forms import BancoForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.db.models.deletion import ProtectedError


@login_required
def banco_list(request):
    bancos = Banco.objects.all()
    return render(request, "bancos/list.html", {"bancos": bancos})


@login_required
def banco_create(request):
    if request.method == "POST":
        form = BancoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bancos:list")
    else:
        form = BancoForm()

    return render(request, "bancos/form.html", {"form": form})


@login_required
def banco_delete(request, pk):
    banco = get_object_or_404(Banco, pk=pk)

    if request.method == "POST":
        try:
            banco.delete()
            messages.success(request, "Banco eliminado correctamente.")
            return redirect("bancos:list")
        except ProtectedError:
            messages.error(
                request,
                "No se puede eliminar el banco porque tiene clientes o créditos asociados.",
            )
            return redirect("bancos:list")

    return render(
        request,
        "bancos/confirm_delete.html",
        {"banco": banco},
    )
