from django.forms import ModelForm, TextInput, NumberInput
from .models import Books


class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ['name', 'author', 'price']

        widgets = {
            "name": TextInput(),
            "author": TextInput(),
            "price": NumberInput()
        }