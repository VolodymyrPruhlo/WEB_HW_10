from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import AuthorForm
from django.contrib.auth.decorators import login_required
from .models import Author
# Create your views here.

@login_required(login_url='/users/login/')
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes:main')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

@login_required(login_url='/users/login/')
def delete_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == "POST":
        author.delete()
        return redirect(reverse('quotes:main'))  # Припускаємо, що ви маєте такий шлях
    return render(request, 'authors/confirm_delete.html', {'object': author})