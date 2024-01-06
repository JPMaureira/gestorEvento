from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import UsuarioPersonalizado



class SignUpForm(UserCreationForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['username', 'nombre', 'email', 'password', 'password2']

class SignInForm(AuthenticationForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ('username', 'password')