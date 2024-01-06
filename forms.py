from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

UsuarioPersonalizado = get_user_model()

class SignUpForm(UserCreationForm):
    nombre = forms.CharField(max_length=100, required=True)

    class Meta:
        model = UsuarioPersonalizado
        fields = ('nombre', 'email', 'password')

class SignInForm(AuthenticationForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ('username', 'password')