"""Urls for users app"""

from django.urls import path, include

from .import views
app_name = "users"

urlpatterns = [
    # Include default auth urls.
    path('users/', include('django.contrib.auth.urls')),
    # Url for redirect page.
    path('users/', views.redirects, name = 'redirects'),
    # Let user see his details
    path('users/details', views.details, name = 'details'),
]