from django.shortcuts import render


def create_account_page(request):
    context = {
        'title': 'Criar Conta'
    }
    
    return render(request, 'users/pages/create-account-page.html', context)
