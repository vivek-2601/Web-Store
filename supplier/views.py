from django.shortcuts import render, redirect

from store.models import Product
from .forms import ProductForm


# Create your views here.
def products(request):
    """The home page for store. Show all the products."""
    products = Product.objects.order_by('name')
    context = {'products': products}
    return render(request, 'supplier/products.html', context)


def new_product(request):
    """Add a ner Product."""
    if request.method != 'POST':
        # No data submitted; create blank from.
        form = ProductForm()

    else:
        # POST data submitted; process data.
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier:products')

    # Display a blan or invalid form.
    context = { 'form': form}
    return render(request, 'supplier/new_product.html', context)