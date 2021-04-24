from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import AddrForm, OrderForm

# Create your views here.
@login_required(login_url='users:login')
def product(request, pro_id):
    """Page for individual product"""
    product = Product.objects.get(id = pro_id)
    if  request.method != 'POST':
        form = OrderForm()
    
    else:
        form = OrderForm(data = request.POST)
        if form.is_valid():
            odr = form.save(commit = False)
            odr.user = request.user
            odr.product = Product.objects.get(id = pro_id)
            # update product quantites
            product = Product.objects.get(id=pro_id)
            if(product.rem_quant - odr.quantity>=0):
                product.rem_quant = product.rem_quant - odr.quantity
                product.save()
                odr.save()
            else:
                context = {'required': odr.quantity,'remaining':product.rem_quant,'productid':pro_id}
                return render(request, 'store/outofrange.html', context)
            return redirect('store:products')

    context = {"product": product, "form": form}
    return render(request, 'store/product.html', context= context)

def products(request):
    """The home page for store. Show all the products."""
    products = Product.objects.order_by('name')
    context = {'products': products}
    return render(request, 'store/products.html', context)

def register(request):
    """Register a new User"""
    if request.method != 'POST':
        # Display blank registration form.
        form_u = UserCreationForm(prefix= 'user')
        form_a = AddrForm(prefix= 'addr')
    else:
        # Process completed from
        form_u = UserCreationForm(data=request.POST, prefix='user')
        form_a = AddrForm(data=request.POST, prefix= 'addr')
        if form_u.is_valid():
            new_user = form_u.save()
            # Log the new user in and redirect to home page
            login(request, new_user)
            if form_a.is_valid():
                addr = form_a.save(commit=False)
                addr.user = new_user
                addr.save()
            return redirect('store:products')
    # Display a blank or invalid form
    context = {'form_u': form_u, 'form_a': form_a}
    return render(request, 'registration/user_register.html', context)

def search(request):
    if request.method == "GET":
        pro_name = request.GET.get('searchquery','')
        products = Product.objects.filter(name = pro_name)
    return render(request, 'store/search.html',{'products':products,'pro_name':pro_name})
