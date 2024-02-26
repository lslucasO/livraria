from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from utils.django_forms import *


class LoginForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Digite seu nome de usuário')
        add_placeholder(self.fields['password'], 'Digite sua senha')
    
    
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
    
    def clean(self):
        ...