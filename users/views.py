from django.http import Http404
from django.shortcuts import render
from django.urls import reverse
from .forms import RegisterForm


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    
    context = {
        'title': 'Criar Conta',
        'form': form,
        'form_action': reverse(register_create)
    }
    
    return render(request, 'users/pages/register.html', context)


def register_create(request):
    if not request.POST:
        raise Http404()
    
    POST = request.POST 
    # Salvando os dados do usuario por sessão
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)
    
    return render(request, '')
