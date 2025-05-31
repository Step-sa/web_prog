from django.core.paginator import Paginator
from django.shortcuts import render

from manipulate_book.models import Books


def home(request):
    books_list = Books.objects.all()

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if min_price:
        books_list = books_list.filter(price__gte=min_price)
    if max_price:
        books_list = books_list.filter(price__lte=max_price)

    paginator = Paginator(books_list, 3)
    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)

    context = {
        'books': books,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'main_view/home.html', context)