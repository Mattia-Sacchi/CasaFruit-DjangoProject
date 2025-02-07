from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def renderLogin(request):
    return render(request, "login.html")

def tryLogin(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)

    if user is None:
        messages.error(request, "Invalid username or password.")
        return renderLogin(request)
    login(request, user)
    messages.success(request, "Login successful!")
    return redirect("dashboard")
        


def userLogin(request):
    if request.method == "POST":
        return tryLogin(request)
    return renderLogin(request)
