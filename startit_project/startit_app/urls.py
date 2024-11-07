from django.urls import path
from . import views
from .views import BookDetailView, basket_add
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('catalog/', views.catalog, name='catalog' ),
    path('newbooks/', views.catalog, name='new' ),
    path('bestsellers', views.catalog, name='bestsellers' ),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('cart/', views.cart_detail, name='cart_detail' ),
    path('basket_add/<int:book_id>/', views.basket_add, name='basket_add'),
    path('basket_delete/<int:id>/', views.basket_delete, name='basket_delete'),

    
    path('favorites/', views.favorite, name='favorite' ),
    path('favorite_add/<int:book_id>/', views.favorite_add, name='favorite_add'),
    path('favorite_delete/<int:id>/', views.favorite_delete, name='favorite_delete'),
]

