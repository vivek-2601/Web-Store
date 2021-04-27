from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import Permission
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Count, Sum
from django.views.decorators.csrf import csrf_exempt
from store.forms  import AddrForm
from store.models import Product
from store.models import Order
from .forms import ProductForm
from django.http import Http404


# Make a diffrent page for exitsing seller to become seller 
@permission_required('auth.can_sell', login_url='supplier:register')
def products(request):
    """The home page for store. Show all the products."""
    products = Product.objects.filter(owner=request.user).order_by('name')
    context = {'products': products}
    #print(pro)
    return render(request, 'supplier/products.html', context)

@permission_required('auth.can_sell', login_url='supplier:register')
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
        form_u = UserCreationForm(prefix = 'user')
        form_a = AddrForm( prefix = 'addr')
        #print(form_a)
    else:
        # Process completed from
        form_u= UserCreationForm(data=request.POST, prefix = 'user')
        form_a = AddrForm(data = request.POST, prefix = 'addr')

        if form_u.is_valid():
            new_user = form_u.save()
            permission = Permission.objects.get(codename='can_sell')
            new_user.user_permissions.add(permission)
            # Log the new user in and redirect to home page
            if form_a.is_valid():
                #print("yes")
                addr = form_a.save(commit=False)
                addr.user = new_user
                addr.save()
            #print("no")
            login(request, new_user)
            return redirect('users:redirects')
    # Display a blank or invalid form
    context = {'form_u': form_u, 'from_a':form_a}
    return render(request, 'registration/supplier_register.html', context)

@permission_required('auth.can_sell', login_url='supplier:register')
def product(request, pro_id):
    """Seller can see details of their product"""
    product = Product.objects.get( id = pro_id)

    # Make sure product belongs to the current supplier
    if product.owner != request.user:
        raise Http404("404")
    
    return render(request, 'supplier/product.html', {'product':product})

@permission_required('auth.can_sell', login_url='supplier:register')
def edit_pro(request, pro_id):
    '''Edit existing product'''
    product = Product.objects.get( id = pro_id)
   

    if product.owner != request.user:
       raise Http404
    
    if request.method != 'POST':
        # Initial request; pre-fill form with detais
        form = ProductForm(instance = product)

    else:
        # POST data submitted; process data.
        form = ProductForm( instance = product, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier:product', pro_id = pro_id)

    return render(request, 'supplier/edit_pro.html', {'form':form, 'product':product})


@permission_required('auth_can_sell', login_url='supplier:register')
def orders(request):
    user = request.user
    odrs = Order.objects.filter(product__owner = user).values('product__name').annotate(Sum('quantity'))
    totalProductSold = 0
    for o in odrs:
        totalProductSold += o['quantity__sum']
    return render(request, 'supplier/orders.html', {'orders': odrs,'totalProductSold':totalProductSold})
