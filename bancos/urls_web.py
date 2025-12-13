from django.urls import path
from .views_web import banco_list, banco_create
from .views_web import banco_list, banco_create, banco_delete

app_name = "bancos"

urlpatterns = [
    path("", banco_list, name="list"),
    path("crear/", banco_create, name="create"),
    path("<int:pk>/eliminar/", banco_delete, name="delete"),
]
