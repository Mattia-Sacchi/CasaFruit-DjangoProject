from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

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

    if errorMessage != "":
        messages.error(request, errorMessage)
        return renderRegisterPage(request)


    user = User.objects.create_user(username=username, email=email, password=password1)
    user.save()
    messages.success(request, "Account created successfully! Please log in.")
    return redirect("login")



def userRegister(request):
    if request.method == "POST":
        return tryRegister(request)
    return renderRegisterPage(request)
