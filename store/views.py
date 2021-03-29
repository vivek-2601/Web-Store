from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for store."""
    return render(request, 'store/index.html')

def login(request):
    """The home page for store."""
    return render(request, 'store/login.html')

def registration(request):
    """The home page for store."""
    return render(request, 'store/registration.html')

def about(request):
    """The home page for store."""
    return render(request, 'store/about.html')