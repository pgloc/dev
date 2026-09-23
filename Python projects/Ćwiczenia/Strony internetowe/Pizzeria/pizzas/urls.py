"""Definiuje wzorce adresów URL dla pizzas."""
from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
    # Strona główna
    path('', views.index, name='index'),
]