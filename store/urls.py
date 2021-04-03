"""Defines URL patterns for store."""

from django.urls import path, include

from . import views

app_name = 'store'

urlpatterns = [
    # Home page
    path('', views.products, name = 'products'),
    # Include defalult auth urls
    path('users/', include('django.contrib.auth.urls')),
    # New use registration page.
    path('users/register', views.register, name ='register')
]