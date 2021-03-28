"""Defines URL patterns for store."""

from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    # Home page
    path('', views.products, name = 'products'),
]