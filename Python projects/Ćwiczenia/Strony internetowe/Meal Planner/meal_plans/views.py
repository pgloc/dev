from django.shortcuts import render

def index(request):
    """Strona główna dla aplikacji meal_plans."""
    return render(request, 'meal_plans/index.html')