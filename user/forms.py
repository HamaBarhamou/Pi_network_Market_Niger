from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nom d\'utilisateur', widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': 'Nom d\'utilisateur ou mot de passe incorrect',
        'inactive': 'Ce compte est inactif',
    }