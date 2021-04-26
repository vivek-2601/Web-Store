"""Defines URL patterns for store."""

from django.urls import path, include

from . import views

app_name = 'store'

urlpatterns = [
    # Home page
    path('', views.products, name = 'products'),
    # New use registration page.
    path('users/register', views.register, name ='register'),
    # Individual product's page.
    path('<int:pro_id>', views.product, name= 'product'),
    # Product Name By Search Page
    path('store/search/',views.searchByProductName,name='searchByProductName'),
    # Confirm and place order 
    path('store/confirm/<int:pro_id>', views.confirm, name='confirm'),
    # Category Wise Show
    path('store/categorywise/',views.categorywise,name='categorywise'),
    #afterOrderRedirectPage
    path('store/afterOrderRedirect',views.afterOrderRedirect,name='afterOrderRedirect'),
]