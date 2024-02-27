from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from utils.django_forms import *


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Seu nome de usuario')
        add_placeholder(self.fields['email'], 'Seu e-mail')
        add_placeholder(self.fields['first_name'], 'Ex: Lucas')
        add_placeholder(self.fields['last_name'], 'Ex: Santana')
        add_placeholder(self.fields['password'], 'Sua senha deve ser forte')
        add_placeholder(self.fields['confirm_password'], 'Repita sua senha')

    
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
    
    def clean(self):
        # Validando os campos de senha, se são iguais.
        
        cleaned_data = super().clean()
        
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            password_confirmation_error = ValidationError(
                'Password must have at least one uppercase letter, '
                'one lowercase letter and one number. The length should be '
                'at least 8 characters.',
                code='invalid'
            )
            raise ValidationError(
                {
                'password': password_confirmation_error,
                },
            )