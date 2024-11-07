from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default=1)
    year = models.IntegerField()
    summary = models.TextField()
    description = models.TextField(default='Описание отсутствует')
    razdel = models.TextField(default='Нет данных')
    ves = models.TextField(default='Нет данных')
    formatK = models.TextField(default='Нет данных')
    pereplet = models.TextField(default='Нет данных')
    izdatelstvo = models.TextField(default='Нет данных')
    kolvostranits = models.TextField(default='Нет данных')
    price = models.IntegerField(default='Нет данных')
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)  # Поле для загрузки изображений

    def __str__(self):
        return self.title




class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f'Корзина для {self.user.username}'

    def sum(self):
        return self.quantity * self.book.price



class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    


    def __str__(self):
        return f'Корзина для {self.user.username}'

