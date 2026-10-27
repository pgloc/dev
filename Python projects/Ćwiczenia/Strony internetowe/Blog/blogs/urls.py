"""Definiuje wzorce adresów URL dla blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Strona główna.
    path('', views.index, name='index'),
    # Wyświetlenie wszystkich postów.
    path('posts/', views.posts, name='posts'),
    # Strona przeznaczona do dodawania nowego postu.
    path('new_post/', views.new_post, name='new_post'),
    # Strona przeznaczona do edycji postu.
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    # Strona przeznaczona do usuwania postu.
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]