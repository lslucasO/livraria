from django.shortcuts import render
from .forms import RegisterForm

def register_view(request):
    form = RegisterForm()
    
    context = {
        'title': 'Criar Conta',
        'form': form
    }
    
    return render(request, 'users/pages/create-account-page.html', context)
