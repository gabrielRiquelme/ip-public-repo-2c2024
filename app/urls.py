from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index-page'),
    path('home/', views.home, name='home'),
    path('buscar/', views.search, name='buscar'),
    path('register/', views.register_pag,name='register'),
    path('login/', views.login_pag, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('favourites/', views.getAllFavouritesByUser, name='favoritos'),
    path('favourites/add/', views.saveFavourite, name='agregar-favorito'),
    path('favourites/delete/', views.deleteFavourite, name='borrar-favorito'),

    path('exit/', views.exit, name='exit'),
]