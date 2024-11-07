# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'login__input',
        'placeholder': 'Write your email',
        'id': 'login-email',
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'login__input', 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'login__input', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'login__input', 'placeholder': 'Confirm password'}),
        }

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'login__input',
        'placeholder': 'Write your username',
        'id': 'login-email',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'login__input',
        'placeholder': 'Enter your password',
        'id': 'login-pass',
    }))
