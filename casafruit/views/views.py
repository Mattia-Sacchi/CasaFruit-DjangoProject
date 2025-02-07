from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout


def homepage(request):
    return render(request, 'homepage.html')

def logoutRedirect(request):
    logout(request)
    messages.success(request, "Logout successful!")
    
    return redirect("login")
    
