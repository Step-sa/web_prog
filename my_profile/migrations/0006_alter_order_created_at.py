# Generated by Django 5.1.6 on 2025-03-08 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0005_alter_order_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.TextField(default='2025-03-08 22:35'),
        ),
    ]
