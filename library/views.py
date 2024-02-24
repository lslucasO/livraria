from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import *

def home(request):
    
    books = Book.objects.filter(
        is_published=True
        ).order_by('-id')

    context = {
        'title': 'Home',
        'books': books,
    }
    
    return render(request, 'global/partials/home.html', context)


def book_page(request, id):

    book = get_object_or_404(
        Book,
        pk=id,
        is_published=True,
    )
    
    context = {
        'book': book,
        'title': book.title,
    }
    return render(request, 'library/pages/book-page.html', context)
