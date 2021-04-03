from django.shortcuts import render

from store.models import Product
from .forms import ProductForm


# Create your views here.
def products(request):
    """The home page for store. Show all the products."""
    products = Product.objects.order_by('name')
    context = {'products': products}
    return render(request, 'supplier/products.html', context)


