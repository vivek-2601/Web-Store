from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User, Permission

# Create your views here.

def redirects(request):
    # user = User.objects.get(username= kw)
    if(request.user.has_perm('auth.can_sell')):
        return redirect('supplier:products')
    else:
        return redirect('store:products')