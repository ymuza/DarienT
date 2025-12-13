from django.urls import path
from .views_web import cliente_list, cliente_create, cliente_delete

app_name = "clientes"


urlpatterns = [
    path("", cliente_list, name="list"),
    path("crear/", cliente_create, name="create"),
    path("<int:pk>/eliminar/", cliente_delete, name="delete"),
]
