from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def renderRegisterPage(request):
    return render(request, "register.html")

def tryRegister(request):
    username = request.POST["username"]
    email = request.POST["email"]
    password1 = request.POST["password1"]
    password2 = request.POST["password2"]

    errorMessage = ""

    if password1 != password2:
        errorMessage = "Passwords do not match!"

    if User.objects.filter(username=username).exists():
        errorMessage =  "Username already exists!"
    
    if User.objects.filter(email=email).exists():
        errorMessage = "Email already in use!"

    if errorMessage == "":
        messages.error(request, errorMessage)


    user = User.objects.create_user(username=username, email=email, password=password1)
    user.save()
    messages.success(request, "Account created successfully! Please log in.")
    return redirect("login")



def register(request):
    if request.method == "POST":
        return tryRegister(request)
    return renderRegisterPage(request)

def login(request):
    print("porcodio")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("dashboard")  # Redirect to a dashboard or home page
        else:
            messages.error(request, "Invalid username or password.")
        

    return render(request, "login.html")
