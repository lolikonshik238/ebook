from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from .models import Book, Basket, Favorite
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required


def home_page(request):
    books = Book.objects.all()
    context = {
        'books': books
        
    }
    return render(request, "./home.html", context)


# def catalog(request):
#     return render(request, "./catalog.html")



class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    books = Book.objects.all()

    
    context = {
        'books': books,
        
    }

    


def catalog(request):
    genre = request.GET.get('genre')  # Получаем жанр из запроса, если он есть
    if genre:
        books = Book.objects.filter(genre__name=genre)  # Фильтруем книги по жанру
    else:
        books = Book.objects.all()  # Показываем все книги, если жанр не выбран

    genres = Book.objects.values_list('genre__name', flat=True).distinct()  # Получаем уникальные жанры
    return render(request, 'catalog.html', {'books': books, 'genres': genres})



def newbooks(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, "./newbooks.html", context)


def bestsellers(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, "./newbooks.html", context)



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')  # Переход на главную страницу после регистрации
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('home_page')  # Переход на главную страницу после успешного входа
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('home_page')


def cart_detail(request):
    books = Book.objects.all()
   
    context = {
        'baskets': Basket.objects.filter(user=request.user),
        'books': books
    }

    return render(request, 'cart_detail.html', context)


def basket_add(request, book_id):
    book = Book.objects.get(id=book_id)  # Получаем книгу по ID
    # Измените user_request на request
    baskets = Basket.objects.filter(user=request.user, book=book)  

    if not baskets.exists():  # Если корзина пуста
        Basket.objects.create(user=request.user, book=book, quantity=1)  # Создаем новую запись в корзине
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # Перенаправляем на предыдущую страницу
    else:  # Если запись уже существует
        basket = baskets.first()  # Получаем первую запись
        basket.quantity += 1  # Увеличиваем количество
        basket.save()  # Сохраняем изменения
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # Перенаправляем на предыдущую страницу


def basket_delete(request, id):
    basket = Basket.objects.get(id = id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




def favorite(request):
    books = Book.objects.all()
    
    context = {
        'favorites': Favorite.objects.filter(user=request.user),
        'books': books
    }

    return render(request, 'favorite.html', context)

def favorite_add(request, book_id):
    book = Book.objects.get(id=book_id)  # Получаем книгу по ID
    # Измените user_request на request
    favorites = Favorite.objects.filter(user=request.user, book=book)  

    if not favorites.exists():  # Если корзина пуста
        Favorite.objects.create(user=request.user, book=book, )  # Создаем новую запись в корзине
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # Перенаправляем на предыдущую страницу
    else:  # Если запись уже существует
        favorite = favorites.first()  # Получаем первую запись
        
        favorite.save()  # Сохраняем изменения
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # Перенаправляем на предыдущую страницу


def favorite_delete(request, id):
    favorite = Favorite.objects.get(id = id)
    favorite.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


