from django import forms
from django.forms import ModelForm, Textarea, NumberInput
from django.contrib.auth.forms import UserCreationForm
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(
                    label="Nom d'utilisateur",
                    max_length=30,
                    widget=forms.TextInput(attrs={
                                            'class': 'form-control'
                                            })
                    )
    password = forms.CharField(
                    label="Mot de passe",
                    widget=forms.PasswordInput(attrs={
                                                'class': 'form-control'
                                                })
                    )

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')