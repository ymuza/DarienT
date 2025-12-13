from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Credito
from .forms import CreditoForm


@login_required
def credito_list(request):
    creditos = (
        Credito.objects
        .select_related("cliente", "banco")
        .all()
    )
    return render(request, "creditos/list.html", {"creditos": creditos})


@login_required
def credito_create(request):
    if request.method == "POST":
        form = CreditoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Crédito creado correctamente.")
            return redirect("creditos:list")
    else:
        form = CreditoForm()

    return render(request, "creditos/form.html", {"form": form})


@login_required
def credito_delete(request, pk):
    credito = get_object_or_404(Credito, pk=pk)

    if request.method == "POST":
        credito.delete()
        messages.success(request, "Crédito eliminado correctamente.")
        return redirect("creditos:list")

    return render(
        request,
        "creditos/confirm_delete.html",
        {"credito": credito},
    )
