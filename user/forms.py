from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    USER_TYPE_CHOICES = (
        (2, 'Vendor'),
        (3, 'Customer'),
    )

    fonction = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'fonction','phone_number']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.fonction = self.cleaned_data['fonction']
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nom d\'utilisateur', widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': 'Nom d\'utilisateur ou mot de passe incorrect',
        'inactive': 'Ce compte est inactif',
    }