from django.shortcuts import render
from .forms import RegisterForm

def register_view(request):
    context = {
        'title': 'Criar Conta'
    }
    
    return render(request, 'users/pages/create-account-page.html', context)
