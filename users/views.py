from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm


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


def login_view(request):
    
    form = LoginForm()
    
    context = {
        'title': 'Logar',
        'form': form,
        'form_action': reverse('users:login-create')
    }
    
    return render(request, 'users/pages/login.html', context)


def login_create(request):
    if not request.POST:
        raise Http404()
    
    form = LoginForm(request.POST)
    login_url = reverse('users:login')
    
    # Autenticando o usuario no sistema pelo form de Login
    if form.is_valid():
        authenticated_user = authenticate(
            # Puxando nome e senha do usuario do banco de dados
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )
        
        if authenticated_user is not None:
            # Se o usuario for válido com o banco de dados
            messages.success(request, 'Você logou na sua conta.')
            # Inicia a sessão do usuario, metodo login
            login(request, authenticated_user)
        else:
            messages.error(request, 'Credenciais inválidas, tente novamente.')
    else:
        messages.error(request, 'Erro ao validar o formulário.')
    
    return redirect(reverse('users:profile'))



def profile(request):
    return render(request, 'users/pages/profile.html')