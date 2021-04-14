from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import Permission
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from store.models import Product
from .forms import ProductForm


# Make a diffrent page for exitsing seller to become seller 
@permission_required('auth.can_sell', login_url='supplier:register')
def products(request):
    """The home page for store. Show all the products."""
    products = Product.objects.filter(owner=request.user).order_by('name')
    context = {'products': products}
    return render(request, 'supplier/products.html', context)


def new_product(request):
    """Add a ner Product."""
    if request.method != 'POST':
        # No data submitted; create blank from.
        form = ProductForm()

    else:
        # POST data submitted; process data.
        form = ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            new_prod = form.save(commit=False)
            new_prod.owner = request.user
            new_prod.save()
            return redirect('supplier:products')

    # Display a blan or invalid form.
    context = { 'form': form}
    return render(request, 'supplier/new_product.html', context)




def register(request):
    """Register a new Seller"""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed from
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            permission = Permission.objects.get(codename='can_sell')
            new_user.user_permissions.add(permission)
            # Log the new user in and redirect to home page
            login(request, new_user)
            return redirect('users:redirects', kw = new_user.username)
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'registration/supplier_register.html', context)