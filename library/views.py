from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import *

def home(request):
    
    books = Book.objects.filter(is_published=True)

    context = {
        'title': 'Home',
        'books': books,
    }
    
    return render(request, 'global/partials/home.html', context)

