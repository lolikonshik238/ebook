from django.contrib import admin
from .models import Book, Basket, Genre, Favorite

admin.site.register(Book)
admin.site.register(Basket)
admin.site.register(Genre)
admin.site.register(Favorite)