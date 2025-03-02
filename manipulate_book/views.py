from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import BooksForm
from .models import Books
from django.contrib.auth.decorators import login_required, user_passes_test


def is_admin(user):
    return user.is_authenticated and user.role == 'admin'


@user_passes_test(is_admin, login_url='/profile/login/')
def edit_book(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    if request.method == 'POST':
        form = BooksForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(reverse('main_view:home'))
    form = BooksForm(instance=book)
    return render(request, 'manipulate_book/edit.html', {'form': form})


@user_passes_test(is_admin, login_url='/profile/login/')
def delete_book(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    book.delete()
    return redirect('main_view:home')


@login_required(login_url='/profile/login/')
def add_book(request):
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('main_view:home'))
    form = BooksForm()
    return render(request, 'manipulate_book/add.html', {'form': form})
