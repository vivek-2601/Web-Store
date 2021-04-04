from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import Product

# Create your views here.
def products(request):
    """The home page for store. Show all the products."""
    products = Product.objects.order_by('name')
    context = {'products': products}
    return render(request, 'store/products.html', context)

def register(request):
    """Register a new User"""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed from
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the new user in and redirect to home page
            login(request, new_user)
            return redirect('store:products')
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'registration/user_register.html', context)


