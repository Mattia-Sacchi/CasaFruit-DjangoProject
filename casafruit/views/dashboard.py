from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from ..models import Like, Product

def BoolFromString(s):
    s = s.lower()  # Handle case-insensitivity

    if s in ('true', '1', 't', 'y', 'yes', 'on'):  # Add more if needed
        return True
    elif s in ('false', '0', 'f', 'n', 'no', 'off'):  # Add more if needed
        return False
    else:
        # Handle invalid input (raise an exception, return a default, etc.)
        raise ValueError(f"Invalid boolean string: {s}")  # Or return None, or False, etc.


def likeChanged(request):
    like = BoolFromString(request.POST["like"])
    productName = request.POST["product"]

    prod = Product.objects.get(name=productName)
    print(like)

    if prod is None:
        messages.error(request, 'Somenthing went wrong with this product')
        return renderDash(request)
    
    objs = Like.objects.filter(product = prod, user= request.user )

    if len(objs) == 0:
        obj = Like(product = prod,user = request.user ,like = like )
    else:
        obj = objs.first() # and only ;)
        obj.like = like
    obj.save()
    
    print(obj)
    return renderDash(request)

def getLikesDict(prods, likes, user):
    dict = {}
    for p in prods:
        dict[p] = False

    for l in likes:
        if l.user != user:
            continue
        contained = False
        for p in prods:
            if p == l.product:
                dict[p] = l.like
                contained = True
        if contained == False:
                dict[p] = False
    return dict
            

    
        
def renderDash(request):
    likes = Like.objects.all()
    products = Product.objects.all()
    likesDict = getLikesDict(products,likes,request.user)
    print(likesDict)

    
    return render(request, 'dashboard.html', {'products': products, 'likes' : likes})

def dashboardPage(request):
    if request.method == "POST":
        return likeChanged(request)

    return renderDash(request)