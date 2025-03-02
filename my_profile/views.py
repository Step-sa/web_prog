from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm
# Create your views here.


def my_profile(request):
    return render(request, 'my_profile/profile.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect(reverse('main_view:home'))
    else:
        form = RegisterForm()
    return render(request, 'my_profile/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('main_view:home'))
    else:
        form = LoginForm()
    return render(request, 'my_profile/login.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect(reverse('main_view:home'))
