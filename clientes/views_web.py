from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import Cliente
from .forms import ClienteForm


@login_required
def cliente_list(request):
    clientes = Cliente.objects.select_related("banco").all()
    return render(request, "clientes/list.html", {"clientes": clientes})


@login_required
def cliente_create(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clientes:list")
    else:
        form = ClienteForm()

    return render(request, "clientes/form.html", {"form": form})



@login_required
def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == "POST":
        cliente.delete()
        messages.success(request, "Cliente eliminado correctamente.")
        return redirect("clientes:list")

    return render(
        request,
        "clientes/confirm_delete.html",
        {"cliente": cliente},
    )
