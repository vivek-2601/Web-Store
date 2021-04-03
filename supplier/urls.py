"""Defines URL patterns for supplier."""

from django.urls import path, include

from .import views

app_name = 'supplier'

urlpatterns = [
    # Home page
    path('supplier/', views.products, name = 'products'),
    # Page for adding a new product
    path('supplier/new_product', views.new_product, name = 'new_product'),
    # Include default auth urls.
    path('supplier/', include('django.contrib.auth.urls')),
    # Registration page.
    path('supplier/register', views.register, name = 'register')
]