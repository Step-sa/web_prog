# Generated by Django 5.1.6 on 2025-03-15 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manipulate_book', '0003_alter_books_price'),
        ('my_profile', '0008_alter_order_created_at_alter_orderitem_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manipulate_book.books'),
        ),
    ]
