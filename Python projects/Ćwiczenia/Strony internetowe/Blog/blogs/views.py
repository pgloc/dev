from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import PostForm

def index(request):
    """Strona główna dla aplikacji Blog."""
    return render(request, 'blogs/index.html')

def posts(request):
    """Wyświetlenie wszystkich postów."""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)

def new_post(request):
    """Dodaj nowy post."""
    if request.method != 'POST':
        # Nie przekazano żadnych danych, należy utworzyć pusty formularz.
        form = PostForm()
    else:
        # Przekazano dane za pomocą żądania POST, należy je przetworzyć.
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:posts')

    # Wyświetlenie pustego formularza.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

def edit_post(request, post_id):
    """Edycja istniejącego postu."""
    post = BlogPost.objects.get(id=post_id)

    if request.method != 'POST':
        # Nie przekazano żadnych danych, należy utworzyć pusty formularz.
        form = PostForm(instance=post)
    else:
        # Przekazano dane za pomocą żądania POST, należy je przetworzyć.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:posts')

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)