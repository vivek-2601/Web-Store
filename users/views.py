from django.shortcuts import render, redirect
from django.db.models import F
from store.models import Product,Address,Order
from django.contrib.auth.decorators import login_required

# Create your views here.

def redirects(request):
    """Redirects  user to apropriate page after log in."""
    if(request.user.has_perm('auth.can_sell')):
        return redirect('supplier:products')
    else:
        return redirect('store:products')

@login_required(login_url= 'users:login')
def details(request):
    """Allows user to see his details and order history"""
    if request.method == 'POST':
        sortingmethod = request.POST.get('sortingmethod','')
        sortingOrder = request.POST.get('sortingOrder','')
        addr = Address.objects.get(user = request.user)
        if(sortingmethod=='Alphabatical Order Of Product Name'):
            if(sortingOrder=='Ascending'):
                odrs = Order.objects.filter(user = request.user).values('product__name', 'quantity', 'product__unitprice', 'date').order_by('product__name')      
            else:
                odrs = Order.objects.filter(user = request.user).values('product__name', 'quantity', 'product__unitprice', 'date').order_by('-product__name')
        elif(sortingmethod=='Amount Payed'):
            if(sortingOrder=='Ascending'):
                odrs = Order.objects.filter(user = request.user).values('product__name', 'quantity', 'product__unitprice', 'date').order_by(F('product__unitprice')*F('quantity'))      
            else:
                odrs = Order.objects.filter(user = request.user).values('product__name', 'quantity', 'product__unitprice', 'date').order_by(-F('product__unitprice')*F('quantity'))
        elif(sortingmethod=='Order Time'):
            if(sortingOrder=='Ascending'):
                odrs = Order.objects.filter(user = request.user).values('product__name', 'quantity', 'product__unitprice', 'date').order_by('date')      
            else:
                odrs = Order.objects.filter(user = request.user).values('product__name', 'quantity', 'product__unitprice', 'date').order_by('-date')
        else:
            sortingmethod = "Order Time"
            sortingOrder = "Descending"
            odrs = Order.objects.filter(user = request.user).values('product__name', 'quantity', 'product__unitprice', 'date').order_by('date')
        context = {'address': addr, 'orders':odrs,'sortingmethod':sortingmethod,'sortingOrder':sortingOrder}
        return render(request, 'users/details.html', context)
    else:
        sortingmethod = "Order Time"
        sortingOrder = "Ascending"
        addr = Address.objects.get(user = request.user)
        odrs = Order.objects.filter(user = request.user).values('product__name', 'quantity', 'product__unitprice', 'date').order_by('date')
        context = {'address': addr, 'orders':odrs,'sortingmethod':sortingmethod,'sortingOrder':sortingOrder}
        return render(request, 'users/details.html', context)
    