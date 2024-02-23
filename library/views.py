from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import *

def home(request):
    context = {
        'title': 'Home'
    }
    
    return render(request, 'global/partials/home.html', context)