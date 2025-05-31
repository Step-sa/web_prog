from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from manipulate_book.models import Books
from django.utils import timezone
class CustomUser(AbstractUser):
    ROLES = (
        ('user', 'Обычный пользователь'),
        ('admin', 'Администратор'),
    )

    display_name = models.CharField(max_length=100, verbose_name="Отображаемое имя")
    role = models.CharField(max_length=10, choices=ROLES, default='user')

    def __str__(self):
        return self.display_name

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(default=timezone.now())
    total_price = models.PositiveIntegerField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def get_cost(self):
        return self.price * self.quantity