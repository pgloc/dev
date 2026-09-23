"""Definiuje wzorce adresów URL dla pizzas."""
from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
    # Strona główna
    path('', views.index, name='index'),
    # Wyświetlenie wszystkich pizz.
    path('pizzas/', views.pizzas, name='pizzas'),
    # Strona szczegółowa dotycząca pojedynczej pizzy.
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]