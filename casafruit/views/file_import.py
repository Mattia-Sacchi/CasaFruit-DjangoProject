from django.shortcuts import render, redirect
from django.contrib import messages
from zipfile import ZipFile
from ..models import Product
import json
DataFilePath = 'media/objs/'
DataFileName = 'data.json'

def tryFileImport(request):
        
    if 'zip' not in request.FILES:
        messages.error(request, "Something went wrong with the uploading")
        return render(request, 'settings.html')

    uploaded_file = request.FILES['zip']

    with ZipFile(file=uploaded_file, mode='r') as zip: 
    # printing all the contents of the zip file 

        zip.printdir()

        namelistZip = zip.namelist()
        if DataFileName not in namelistZip:
            messages.error(request, "Config file missing")
            return render(request, 'settings.html')

        products = Product.objects.all()
        
        zip.extract(DataFileName, path=DataFilePath)

        with open(DataFilePath+DataFileName, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                name = item['name']
                price = item['price']
                description = item['description']
                image = item['image']

                alreadyPresent = False
                for prod in products:
                    if prod.name == name or prod.image == image:
                        alreadyPresent = True
                        break
                if alreadyPresent:
                    messages.error(request, name+ ' already present in db')
                    continue

                if image not in namelistZip:
                    messages.error(request, image+ ' was not found')
                    continue

                temp = Product(name=name,price=price,description=description,image= image)
                temp.image = "products/" +image
                temp.save()
                zip.extract(image,"media/products")
                messages.info(request, name+ ' is added to the db')
                

    return render(request, 'settings.html')

def processFileZip(request):
    if request.method == "POST":
        return tryFileImport(request)

def fileImport(request):
    return render(request, 'settings.html')
