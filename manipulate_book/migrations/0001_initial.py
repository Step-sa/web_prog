# Generated by Django 5.1.6 on 2025-02-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('author', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
