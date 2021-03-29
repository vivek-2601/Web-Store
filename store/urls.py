"""Defines URL patterns for store."""

from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    # Home page
    path('', views.index, name = 'index'),
    path('registration/', views.registration, name = 'registration'),
    path('login/', views.login, name = 'login'),
    path('about/', views.about, name = 'about'),
]