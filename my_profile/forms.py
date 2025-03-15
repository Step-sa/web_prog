from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    display_name = forms.CharField(max_length=100, required=True, label="Отображаемое имя")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'display_name', 'password1', 'password2', 'role']


class LoginForm(AuthenticationForm):
    pass


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'display_name']
        widgets = {
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
            'display_name': forms.TextInput(),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Введите старый пароль", widget=forms.PasswordInput())
    new_password1 = forms.CharField(label="Введите новый пароль", widget=forms.PasswordInput())
    new_password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput())
