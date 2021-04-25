from django.shortcuts import render, redirect
from store.models import *


# Create your views here.

def redirects(request):
    """Redirects  user to apropriate page after log in."""
    if(request.user.has_perm('auth.can_sell')):
        return redirect('supplier:products')
    else:
        return redirect('store:products')

def details(request):
    """Allows user to see his details and order history"""
    addr = Address.objects.get(user = request.user)
    odrs = Order.objects.filter(user = request.user).values('product__name', 'quantity', 'product__unitprice', 'date')

    context = {'address': addr, 'orders':odrs}
    return render(request, 'users/details.html', context )