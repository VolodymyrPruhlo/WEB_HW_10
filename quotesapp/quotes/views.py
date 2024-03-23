from django.urls import path
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .models import Tag, Quote
from authors.models import Author
from django.db.models import Count
from django.core.paginator import Paginator
from .forms import TagForm, QuoteForm


def main(request):
    quotes = Quote.objects.all()
    tags_with_counts = Tag.objects.annotate(num_quotes=Count('quote'))
    most_common_tags = tags_with_counts.order_by('-num_quotes')[:10]
    paginator = Paginator(quotes, 10)  # розділяємо всі цитати на сторінки, по 10 цитат на сторінку
    page_number = request.GET.get('page')  # отримуємо номер поточної сторінки
    page_obj = paginator.get_page(page_number)
    context = {
        'quotes': quotes,
        'most_common_tags': most_common_tags,
        'page_obj': page_obj,
    }
    return render(request, 'quotes/index.html', context)


def quotes_by_tag_view(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    quotes = tag.quote_set.all()
    context = {
        'tag': tag,
        'quote': quotes,
    }
    return render(request, 'quotes/quotes_by_tag.html', context)


def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    context = {
        'author': author,
        'name': author.name,
        'born_date': author.born_date,
        'born_location': author.born_location,
        'description': author.description,
    }
    return render(request, 'quotes/author_detail.html', context)

@login_required(login_url='/users/login/')
def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes:main')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})

@login_required(login_url='/users/login/')
def add_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes:main')
    else:
        form = TagForm()
    return render(request, 'quotes/add_tag.html', {'form': form})

@login_required(login_url='/users/login/')
def delete_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    if request.method == "POST":
        quote.delete()
        return redirect(reverse('quotes:main'))
    return render(request, 'quotes/confirm_delete.html', {'object': quote})