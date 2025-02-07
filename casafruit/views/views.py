from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from ..models import Product
from django.contrib.auth import authenticate,logout


def dashboard(request):
    if str(request.user) != "AnonymousUser":
        print(request.user)
        user = User.objects.get(username=request.user)
    else:
        return render(request, 'dashboard.html')

    if not user.is_authenticated:
        return render(request, 'dashboard.html')
    
    products = Product.objects.all()  # Fetch all products
    return render(request, 'dashboard.html', {'products': products, 'user': user , 'username' : user.get_username()})


def homepage(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'homepage.html', {'products': products})

def logoutRedirect(request):
    logout(request)
    return redirect("login")
    
