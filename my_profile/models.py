from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLES = (
        ('user', 'Обычный пользователь'),
        ('admin', 'Администратор'),
    )

    display_name = models.CharField(max_length=100, verbose_name="Отображаемое имя")
    role = models.CharField(max_length=10, choices=ROLES, default='user')

    def __str__(self):
        return self.display_name