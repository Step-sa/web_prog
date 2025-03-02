from django.core.paginator import Paginator
from django.shortcuts import render

from manipulate_book.models import Books

def home(request):
    books_list = Books.objects.all()
    paginator = Paginator(books_list, 3)
    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)
    return render(request, 'main_view/home.html', {'books': books})