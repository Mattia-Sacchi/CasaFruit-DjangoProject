from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from ..models import Product


def dashboardPage(request):
    if request.method == "POST":
        request.POST['']
    products = Product.objects.all()  # Fetch all products
    return render(request, 'dashboard.html', {'products': products})

