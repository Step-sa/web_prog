from django.urls import path
from . import views

app_name = "my_profile"

urlpatterns = [
    path('', views.my_profile, name="profile"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
]