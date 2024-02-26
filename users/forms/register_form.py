from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from utils.django_forms import *


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
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
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'input-text',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'input-text',
            }),
            'username': forms.TextInput(attrs={
                'class': 'input-text',
            }),'email': forms.TextInput(attrs={
                'class': 'input-text',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'input-text',
            })
        }
        
        
        help_texts = {
            'password': '''
                A senha deve conter pelo menos uma letra maiúscula, uma letra minúscula e um número. O comprimento deve ter pelo menos 8 caracteres.
            '''
        }
    ...