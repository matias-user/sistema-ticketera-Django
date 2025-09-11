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
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu contraseña'})
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repite tu contraseña'})
    )
    class Meta:
        model = CustomUser
        fields = ['name','dni','username','lastname']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
            'lastname': forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido'}),
            'dni': forms.TextInput(attrs={'class':'form-control','placeholder':'99999999-9'}),
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'usuario_1'}),
        }