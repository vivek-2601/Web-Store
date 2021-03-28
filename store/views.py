from django.shortcuts import render

# Create your views here.
def products(request):
    """The home page for store."""
    return render(request, 'store/products.html')