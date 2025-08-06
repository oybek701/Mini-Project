from django.urls import path
from .views import data_list, data_create, data_update, data_delete

urlpatterns = [
    path("", data_list, name="data_list"),
    path("create/", data_create, name="data_create"),
    path("<int:pk>/update/", data_update, name="data_update"),
    path("<int:pk>/delete/", data_delete, name="data_delete"),
]
