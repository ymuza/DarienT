from django.urls import path
from .views_web import credito_list, credito_create, credito_delete

app_name = "creditos"

urlpatterns = [
    path("", credito_list, name="list"),
    path("crear/", credito_create, name="create"),
    path("<int:pk>/eliminar/", credito_delete, name="delete"),
]
