from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    
    class Meta:
        # Modelo padrão de form do Django
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        
        help_texts = {
            'password': '''
                A senha deve conter pelo menos uma letra maiúscula, uma letra minúscula e um número. O comprimento deve ter pelo menos 8 caracteres.
            '''
        }
    ...