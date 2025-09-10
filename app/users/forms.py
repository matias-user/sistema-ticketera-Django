from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput( 
            attrs={
                'class':'form-control',
                'placeholder':'Nombre de usuario'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Contraseña'
            }
        )
    )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name','dni','username','password']