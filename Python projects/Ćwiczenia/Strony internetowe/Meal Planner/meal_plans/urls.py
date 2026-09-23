"""Definiuje wzorce adresów URL dla meal_plans."""
from django.urls import path
from . import views

app_name = 'meal_plans'
urlpatterns = [
    # Strona główna
    path('', views.index, name='index'),
]