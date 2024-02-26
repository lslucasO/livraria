from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from .forms import RegisterForm


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    
    context = {
        'title': 'Criar Conta',
        'form': form,
        'form_action': reverse('users:register-create'),
    }
    
    return render(request, 'users/pages/register.html', context)


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST 
    # Salvando os dados do usuario por sessão
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)
    
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Seu usuário foi criado. Por favor, logue na sua conta.')
        
        del(request.session['register_form_data'])
        
    return redirect(reverse('users:login'))


def login(request):
    context = {
        'title': 'Logar'
    }
    
    return render(request, 'users/pages/login.html', context)