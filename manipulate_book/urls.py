from django.urls import path, reverse

from . import views

app_name = "manipulate_book"

urlpatterns = [
    path('add/', views.add_book, name="add"),
    path('edit/<int:book_id>/', views.edit_book, name="edit"),
    path('delete/<int:book_id>/', views.delete_book, name="delete"),
]