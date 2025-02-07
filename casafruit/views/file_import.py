from django.shortcuts import render, redirect
from django.contrib import messages
from zipfile import ZipFile

def tryFileImport(request):
        
    if 'zip' not in request.FILES:
        messages.error(request, "Something went wrong with the uploading")
        return render(request, 'settings.html')

    uploaded_file = request.FILES['zip']
    print(uploaded_file)
    with ZipFile(file=uploaded_file, mode='r') as zip: 
    # printing all the contents of the zip file 
        zip.printdir()

        #print('Extracting all the files now...') 
        #zip.extractall() 
        #print('Done!') 
    return render(request, 'settings.html')

def processFileZip(request):
    if request.method == "POST":
        return tryFileImport(request)

def fileImport(request):
    return render(request, 'settings.html')
