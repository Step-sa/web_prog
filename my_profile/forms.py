from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    display_name = forms.CharField(max_length=100, required=True, label="Отображаемое имя")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'display_name', 'password1', 'password2', 'role']

class LoginForm(AuthenticationForm):
    pass