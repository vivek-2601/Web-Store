"""Defines URL patterns for supplier."""

from django.urls import path

from .import views

app_name = 'supplier'

urlpatterns = [
    # Home page
    path('supplier/', views.products, name = 'products'),
   
]