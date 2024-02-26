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
                Password must have at least one uppercase letter,
                one lowercase letter and one number. The length should be at least 8 characters.
            '''
        }
    ...