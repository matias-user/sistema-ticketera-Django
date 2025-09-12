from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from common.forms import BootstraClassespMixin
from users.models import CustomUser

class CustomLoginForm(BootstraClassespMixin, AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput( 
            attrs={
                'placeholder':'Nombre de usuario'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )


class CustomUserCreationForm(BootstraClassespMixin, UserCreationForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingresa tu contraseña'})
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Repite tu contraseña'})
    )
    class Meta:
        model = CustomUser
        fields = ['name','dni','username','lastname']
        widgets = {
            'name': forms.TextInput(attrs={ 'placeholder':'Nombre'}),
            'lastname': forms.TextInput(attrs={ 'placeholder':'Apellido'}),
            'dni': forms.TextInput(attrs={ 'placeholder':'99999999-9'}),
            'username': forms.TextInput(attrs={ 'placeholder':'usuario_1'}),
        }