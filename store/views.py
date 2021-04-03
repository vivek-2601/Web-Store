from django.shortcuts import render

from .models import Product

# Create your views here.
def products(request):
    """The home page for store. Show all the products."""
    products = Product.objects.order_by('name')
    context = {'products': products}
    return render(request, 'store/products.html', context)




