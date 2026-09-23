from django.shortcuts import render
from .models import Topic

def index(request):
    """Strona główna dla aplikacji Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Wyświetlenie wszystkich tematów."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Wyświetlenie pojedynczego tematu i wszystkich powiązanych z nim wpisów."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)