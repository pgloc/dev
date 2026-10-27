from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

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

@login_required
def new_post(request):
    """Dodaj nowy post."""
    if request.method != 'POST':
        # Nie przekazano żadnych danych, należy utworzyć pusty formularz.
        form = PostForm()
    else:
        # Przekazano dane za pomocą żądania POST, należy je przetworzyć.
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:posts')

    # Wyświetlenie pustego formularza.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Edycja istniejącego postu."""
    post = BlogPost.objects.get(id=post_id)
    check_topic_owner(request, post)

    if request.method != 'POST':
        # Nie przekazano żadnych danych, należy utworzyć pusty formularz.
        form = PostForm(instance=post)
    else:
        # Przekazano dane za pomocą żądania POST, należy je przetworzyć.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid() and post.owner == request.user:
            form.save()
            return redirect('blogs:posts')

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

@login_required
def delete_post(request, post_id):
    """Usuwanie istniejącego postu."""
    post = BlogPost.objects.get(id=post_id)

    # Sprawdzenie, czy użytkownik jest właścicielem postu.
    check_topic_owner(request, post)

    if request.method == 'POST':
        post.delete()
        return redirect('blogs:posts')

    context = {'post': post}
    return render(request, 'blogs/delete_post.html', context)

def check_topic_owner(request, post):
    """Upewniamy się, że temat należy do bieżącego użytkownika."""
    if post.owner != request.user:
        raise Http404