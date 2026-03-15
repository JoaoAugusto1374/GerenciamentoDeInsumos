from django.urls import path
from . import views

urlpatterns = [
    path("gerenciamento/", views.inicio, name="gerenciamento")
]