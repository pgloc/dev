from django.shortcuts import render

def index(request):
    """Strona główna dla aplikacji pizzas."""
    return render(request, 'pizzas/index.html')