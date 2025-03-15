from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, UserUpdateForm, CustomPasswordChangeForm
from manipulate_book.models import Books
from .models import Order, OrderItem
from .cart import Cart
# Create your views here.


@login_required(login_url='/profile/login/')
def my_profile(request):
    if request.method == "POST":
        if 'change_info' in request.POST:
            user_form = UserUpdateForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                return redirect(reverse('main_view:home'))
            password_form = CustomPasswordChangeForm(request.user)

        elif 'change_password' in request.POST:
            password_form = CustomPasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                return redirect(reverse('main_view:home'))
            user_form = UserUpdateForm(instance=request.user)
    else:
        user_form = UserUpdateForm(instance=request.user)
        password_form = CustomPasswordChangeForm(request.user)

    return render(request, 'my_profile/profile.html',
                  {'user_form': user_form,
                   'password_form': password_form})


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


def cart_add(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Books, id=book_id)
    cart.add(book)
    return redirect(reverse('my_profile:cart_detail'))


def cart_remove(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Books, id=book_id)
    cart.remove(book)
    return redirect(reverse('my_profile:cart_detail'))


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'my_profile/cart_detail.html',
                  {'cart': cart, 'total': cart.get_total_price()})


@login_required(login_url='/profile/login/')
def order_create(request):
    cart = Cart(request)

    if not len(cart):
        return redirect(reverse('my_profile:cart_detail'))

    if request.method == 'POST':
        order = Order.objects.create(user=request.user, total_price=cart.get_total_price())
        for item in cart:
            OrderItem.objects.create(
                order=order,
                book=item['book'],
                price=item['price'],
                quantity=item['quantity']
            )
        cart.clear()
        return redirect(reverse('my_profile:order_list'))
    else:
        return render(request, 'my_profile/order_create.html',
                  {'cart': cart})

def orders_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_profile/orders_list.html',
                  {'orders': orders})