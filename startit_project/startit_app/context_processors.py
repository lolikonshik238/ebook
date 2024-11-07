from .models import Genre

def genres_context(request):
    genres = Genre.objects.all()  # Получаем все жанры
    return {'genres': genres}  # Возвращаем словарь с жанрами
