from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from ..models import Product
from django.contrib.auth import authenticate,logout


def dashboard(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'dashboard.html', {'products': products})

def settings(request):
    return render(request, 'settings.html')

def homepage(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'homepage.html', {'products': products})

def logoutRedirect(request):
    logout(request)
    messages.success(request, "Logout successful!")
    
    return redirect("login")
    
