from django.shortcuts import render, redirect



# Create your views here.

def redirects(request):
    """Redirects  user to apropriate page after log in."""
    if(request.user.has_perm('auth.can_sell')):
        return redirect('supplier:products')
    else:
        return redirect('store:products')