from django.urls import path
from . import views

app_name = "my_profile"

urlpatterns = [
    path('', views.my_profile, name="profile"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:book_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:book_id>/', views.cart_remove, name='cart_remove'),
    path('orders/', views.orders_list, name='order_list'),
    path('order/create/', views.order_create, name='order_create'),
]